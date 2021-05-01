import sys
import os
import requests
import time

plink = os.environ['PLINK']

characteristic = sys.argv[3].strip("''")
status = 0
output = os.popen('VBoxManage list runningvms')
if "bigSUR" in output.read():
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

            os.popen('VBoxManage startvm "bigSUR"')
            time.sleep(120)
            response = requests.get('http://localhost:8080/motion?screen')
            time.sleep(120)
            os.popen(fr'{plink}')
            sys.exit()
        
        except IOError:
            sys.exit()

    if characteristic == "On" and value == "0" and status == 1:
        os.popen('VBoxManage controlvm "bigSUR" acpipowerbutton')
        time.sleep(20)
        os.popen('VBoxManage.exe controlvm "bigSUR" keyboardputscancode "1c"')
        time.sleep(20)
        response = requests.get('http://localhost:8080/motion?screen')
        sys.exit()

#print("irgendwas stimmt nicht")
sys.exit()
