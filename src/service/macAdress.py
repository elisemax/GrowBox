from getmac import get_mac_address
import os

def get_mac_adress():
    cmd = "hciconfig"
    device_id = "hci0" 
    status, output = subprocess.getstatusoutput(cmd)
    bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
    print("from getmac")
    print(bt_mac)

    return bt_mac

#def get_bluetooth_mac_address():
    