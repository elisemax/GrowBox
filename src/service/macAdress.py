from getmac import get_mac_address
import os
import sys
import subprocess

def get_mac_adress():
    cmd = "hciconfig"
    device_id = "hci0" 
    status, output = subprocess.getstatusoutput(cmd)
    bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()

    return bt_mac


    