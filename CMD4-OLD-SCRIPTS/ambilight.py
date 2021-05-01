import sys
import requests
import os
import math

ip = os.environ['IP'] 
user = os.environ['USR'] 
pw = os.environ['PW']

desktop = os.environ['DESKTOP']
Huepath = os.path.join(desktop, 'nodejs', 'CMD4-PYS', 'Hue.txt')
Brightnesspath = os.path.join(desktop, 'nodejs', 'CMD4-PYS', 'Brightness.txt')
Saturationpath = os.path.join(desktop, 'nodejs', 'CMD4-PYS', 'Saturation.txt')

characteristic = sys.argv[3].strip("''")
charapath = os.path.join(desktop, 'nodejs', 'CMD4-PYS', f'{characteristic}.txt')


def WDH():
    f = open(Huepath, 'r')
    h = ((int(f.read())-7)%360)/360 #((x-farb angleichung)%360 rest ist neuer hue wert)/360 ausgabe von 0-1
    f.close()
    
    f = open(Saturationpath, 'r')
    s = math.pow((int(f.read())/100),0.5) #(x/100)^0.5 um tv saturation settings aus zu gleichen
    f.close()
    
    f = open(Brightnesspath, 'r')
    v = int(f.read())/100
    f.close()
    

    if s == 0.0: v*=255; r, g, b = v, v, v
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: r, g, b = v, t, p
    if i == 1: r, g, b = q, v, p
    if i == 2: r, g, b = p, v, t
    if i == 3: r, g, b = p, q, v
    if i == 4: r, g, b = t, p, v
    if i == 5: r, g, b = v, p, q


    body = f"{{r: {int(r)}, g: {int(g)}, b: {int(b)}}}"
    #print(body)
    response = requests.post(f'http://{ip}:1925/6/ambilight/cached', data=body)

    sys.exit()    


if sys.argv[1] == "Get":
    f = open(charapath, 'r')
    print(int(f.read()), end='')
    f.close()
    sys.exit()

if sys.argv[1] == "Set":
    value = sys.argv[4].strip("''") 
    if characteristic != "On":
        if characteristic == "Hue":
            h = ((int(value)-7)%360)/360 
            
            f = open(Saturationpath, 'r')
            s = math.pow((int(f.read())/100),0.5)
            f.close()
            
            f = open(Brightnesspath, 'r')
            v = int(f.read())/100
            f.close()

        if characteristic == "Saturation":
            f = open(Huepath, 'r')
            h = ((int(f.read())-7)%360)/360
            f.close()
            
            s = math.pow((int(value)/100),0.5)
            
            f = open(Brightnesspath, 'r')
            v = int(f.read())/100
            f.close

        if characteristic == "Brightness":
            f = open(Huepath, 'r')
            h = ((int(f.read())-7)%360)/360
            f.close()
            
            f = open(Saturationpath, 'r')
            s = math.pow((int(f.read())/100),0.5)
            f.close()
            
            v = int(value)/100
            
        if s == 0.0: v*=255; r, g, b = v, v, v
        i = int(h*6.) # XXX assume int() truncates!
        f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
        if i == 0: r, g, b = v, t, p
        if i == 1: r, g, b = q, v, p
        if i == 2: r, g, b = p, v, t
        if i == 3: r, g, b = p, q, v
        if i == 4: r, g, b = t, p, v
        if i == 5: r, g, b = v, p, q
        
        body = f"{{r: {int(r)}, g: {int(g)}, b: {int(b)}}}"
        #print(body)
        response = requests.post(f'http://{ip}:1925/6/ambilight/cached', data=body)
        
        f = open(charapath, 'w')
        f.write(value)
        f.close()

        WDH() #ohne wdh wird abundzu falsche farbe angezeigt
        
        sys.exit()

    f = open(charapath, 'r')
    status = int(f.read())
    f.close()    

    import time
    from requests.auth import HTTPDigestAuth         

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(f'https://{ip}:1926/6/powerstate', verify=False, auth=HTTPDigestAuth(user, pw))
    
    if 'Standby' in str(response.content):
        if characteristic == "On" and value == "1" and status == 0:

            f = open(Huepath, 'r')
            h = ((int(f.read())-7)%360)/360
            f.close()
            
            f = open(Saturationpath, 'r')
            s = math.pow((int(f.read())/100),0.5)
            f.close()
            
            f = open(Brightnesspath, 'r')
            v = int(f.read())/100  
            f.close()

            if s == 0.0: v*=255; r, g, b = v, v, v
            i = int(h*6.) # XXX assume int() truncates!
            f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
            if i == 0: r, g, b = v, t, p
            if i == 1: r, g, b = q, v, p
            if i == 2: r, g, b = p, v, t
            if i == 3: r, g, b = p, q, v
            if i == 4: r, g, b = t, p, v
            if i == 5: r, g, b = v, p, q
        
            body = f"{{r: {int(r)}, g: {int(g)}, b: {int(b)}}}"
            #print(body)
            response = requests.post(f'http://{ip}:1925/6/ambilight/cached', data=body)

            f = open(charapath, 'w')
            f.write(value)
            f.close()

            sys.exit()
        
        if characteristic == "On" and value == "0" and status == 1:
            #body = "{r: 0, g: 0, b: 0}"
            #print(body)
            #response = requests.post(f'http://{ip}:1925/6/ambilight/cached', data=body)
           
            #wenn licht ausgeht wird tv aus deepsleep in sleep geholt damit aptv arc geht
            data = '{key: Standby}'
            response = requests.post(f'https://{ip}:1926/6/input/key', data=data, verify=False, auth=HTTPDigestAuth(f'{user}', f'{pw}'))
            time.sleep(1) 
            response = requests.post(f'https://{ip}:1926/6/input/key', data=data, verify=False, auth=HTTPDigestAuth(user, pw))
                        
            f = open(charapath, 'w')
            f.write(value)
            f.close()
            sys.exit()

#print("irgendwas stimmt nicht")
sys.exit()
