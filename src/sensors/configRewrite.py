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



def update_wifi(ssid,password): 
    username = getpass.getuser()
    raw = open('/home/' + username + '/GrowBox/src/service/wpa_supplicant.conf', "r+")
    contents = raw.read().split("\n")
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
    str ='country=CZ\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\nnetwork={\n ssid="'+ssid+'"\n psk="'+password+'"\n}'
    raw.write(str)
    raw.close()