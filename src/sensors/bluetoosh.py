
from calendar import c
import socket
import os
import sys
#conf_path = os.getcwd()
#sys.path.append(conf_path)
#sys.path.append(conf_path + '/home/admin/.local/lib/python3.9/') 
import time
import commands
from sensors.wifiUpdate import update_wifi
from sensors.configRewrite import fileRewrite


class Bluetoosh:

    def receiveMessages():
        
        cmd = "hciconfig"
        device_id = "hci0" 
        status, output = commands.getstatusoutput(cmd)
        bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
        print(bt_mac)

        hostMACAddress = 'B8:27:EB:9D:06:25'
        #+mac
        print(hostMACAddress)
    
        port = 2
        backlog = 1
        size = 1024
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((hostMACAddress, port))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.settimeout(30)
        s.listen(backlog)
        os.system('sudo hciconfig hci0 piscan')
        try:
            print('INFO[bluetooth]: started connecting')
            client, adress = s.accept()
            print('INFO[bluetooth]: client accepted')
            
            for x in range(10):
                print('INFO[bluetooth]: waiting for data...')
                data = client.recv(size)
                print('INFO[bluetooth]: got data')
                if (data):
                    print("INFO[bluetooth]: data not null: ")
                    decoded = data.decode('utf-8')
                    parts = decoded.split(',')
                    interface = 'wlan0'
                    name = parts[0]
                    password = parts[1]
                    print(name)
                    print(password)
                    s.close()
                    update_wifi("/home/admin/GrowBox/src/service/wpa_supplicant.conf",name,password)
                    fileRewrite()
        except Exception as e:
            print(e)
            s.close()
            pass