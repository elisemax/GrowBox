import subprocess
import os
import getpass
def fileRewrite():
    
    username = getpass.getuser()
    print('username:')
    print(username)
    #subprocess.call('sudo su');
    subprocess.call('sudo cp -f /home/' + username + '/GrowBox/src/service/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf',shell=True);
    subprocess.call('reboot',shell=True);
