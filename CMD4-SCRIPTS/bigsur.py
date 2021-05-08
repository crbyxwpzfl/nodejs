import requests
import time
import subprocess
#import privates variable
import sys
import os
sys.path.append(os.environ.get('privates'))
import privates

characteristic = sys.argv[3].strip("''")
status = 0

output = subprocess.Popen(['VBoxManage', 'list', 'runningvms'], stdout=subprocess.PIPE)
if "bigSUR" in str(output.stdout.read()):
    status = 1

if sys.argv[1] == "Get":
    print(int(status), end='')
    sys.exit()

if sys.argv[1] == "Set":
    value = sys.argv[4].strip("''")
    if characteristic == "On" and value == "1" and status == 0:
        
        try:
            f = open("N:/sicherungskopien/gists/ahk.txt")
            f.close()
            
            output = subprocess.run(['VBoxManage', 'startvm', "bigSUR"])
            time.sleep(120)
            response = requests.get('http://localhost:8080/motion?screen')
            time.sleep(120)
            output = subprocess.run(['plink', '-batch', '-i', privates.pathtosshkey, 'bigsur@10.3.141.95', "open -a Music.app && open -a Photos.app"])
            sys.exit() 
        
        except IOError:
            sys.exit()

    if characteristic == "On" and value == "0" and status == 1:
        
        output = subprocess.run(['VBoxManage', 'controlvm', "bigSUR", 'acpipowerbutton'])
        time.sleep(20)
        output = subprocess.run(['VBoxManage', 'controlvm', "bigSUR", 'keyboardputscancode', "1c"])
        time.sleep(20)
        response = requests.get('http://localhost:8080/motion?screen')
        sys.exit()

#print("irgendwas stimmt nicht")
sys.exit()
