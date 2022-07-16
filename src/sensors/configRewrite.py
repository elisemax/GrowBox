import subprocess
def fileRewrite():
    subprocess.call('sudo su');
    subprocess.call('cp -f /home/admin/grow/GrowBox/src/service/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf');
    subprocess.call('reboot');
