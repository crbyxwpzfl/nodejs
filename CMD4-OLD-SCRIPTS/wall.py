import sys
import os
import requests
from requests.auth import HTTPDigestAuth

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ip = os.environ['IP'] 
user = os.environ['USR'] 
pw = os.environ['PW']

desktop = os.environ['DESKTOP']
volumepath = os.path.join(desktop, 'nodejs', 'CMD4-PYS', 'volume.txt')

characteristic = sys.argv[3].strip("''")


if sys.argv[1] == "Get":
    if characteristic == "Brightness":
        f = open(volumepath, 'r')
        volume = int(f.read())
        f.close()
        print(volume, end='')

    if characteristic == "On":
        response = requests.get(f'https://{ip}:1926/6/powerstate', verify=False, auth=HTTPDigestAuth(user, pw))
        if "On" in str(response.content):
            print(1, end='')
        if "Standby" in str(response.content):
            print(0, end='')
        sys.exit()

if sys.argv[1] == "Set":
    value = sys.argv[4].strip("''")
    status = 0
    response = requests.get(f'https://{ip}:1926/6/powerstate', verify=False, auth=HTTPDigestAuth(user, pw))
    if "On" in str(response.content):
        status = 1
    
    if characteristic == "Brightness":
        
        data = f"{{ muted: false, current: {int(value)} }}"
        response = requests.post(f'https://{ip}:1926/6/audio/volume', data=data, verify=False, auth=HTTPDigestAuth(user, pw))
        

        f = open(volumepath, 'w')
        f.write(value)
        f.close()

        sys.exit()
    

    if characteristic == "On" and value == "1" and status == 0:
        data = '{key: Standby}'
        response = requests.post(f'https://{ip}:1926/6/input/key', data=data, verify=False, auth=HTTPDigestAuth(user, pw))
        sys.exit()


    if characteristic == "On" and value == "0" and status == 1:
        data = '{key: Standby}'
        response = requests.post(f'https://{ip}:1926/6/input/key', data=data, verify=False, auth=HTTPDigestAuth(user, pw))
        sys.exit()


#print("irgendwas stimmt nicht")
sys.exit()
