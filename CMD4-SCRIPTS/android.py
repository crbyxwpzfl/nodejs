import requests
import time
import subprocess
#import privates variable
import sys
import os
sys.path.append(os.path.abspath("C:/Users/roess/Desktop/private"))
import privates

characteristic = sys.argv[3].strip("''")
status = 0

output = subprocess.Popen(['VBoxManage', 'list', 'runningvms'], stdout=subprocess.PIPE)
if "android" in str(output.stdout.read()):
    status = 1

if sys.argv[1] == "Get":
    print(int(status), end='')
    sys.exit()

if sys.argv[1] == "Set":
    value = sys.argv[4].strip("''")
    if characteristic == "On" and value == "1" and status == 0:
        output = subprocess.run(['VBoxManage', 'startvm', "android"]) 
        time.sleep(5)
        response = requests.get('http://localhost:8080/motion?screen')
        sys.exit()
    
    if characteristic == "On" and value == "0" and status == 1:
        output = subprocess.run(['VBoxManage', 'controlvm', "android", 'savestate'])
        time.sleep(5)
        response = requests.get('http://localhost:8080/motion?screen')
        sys.exit()

#print("irgendwas stimmt nicht")
sys.exit()
