import subprocess
import os
def fileRewrite():
    #subprocess.call('sudo su');
    subprocess.call('sudo cp -f /home/admin/GrowBox/src/service/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf',shell=True);
    subprocess.call('reboot',shell=True);
