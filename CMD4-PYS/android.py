import sys
import os
import requests
import time

characteristic = sys.argv[3].strip("''")
status = 0
output = os.popen('VBoxManage list runningvms')
if "android" in output.read():
    status = 1

if sys.argv[1] == "Get":
    print(int(status), end='')
    sys.exit()

if sys.argv[1] == "Set":
    value = sys.argv[4].strip("''")
    if characteristic == "On" and value == "1" and status == 0:
        os.popen('VBoxManage startvm "android"')
        time.sleep(5)
        response = requests.get('http://localhost:8080/motion?screen')
        sys.exit()
    
    if characteristic == "On" and value == "0" and status == 1:
        os.popen('VBoxManage.exe controlvm "android" savestate')
        time.sleep(5)
        response = requests.get('http://localhost:8080/motion?screen')
        sys.exit()

#print("irgendwas stimmt nicht")
sys.exit()
