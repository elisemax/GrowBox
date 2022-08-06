
from calendar import c
import socket
import os
import sys
#conf_path = os.getcwd()
#sys.path.append(conf_path)
#sys.path.append(conf_path + '/home/admin/.local/lib/python3.9/') 
import time
import service.macAdress
from sensors.wifiUpdate import update_wifi
from sensors.configRewrite import fileRewrite


class Bluetoosh:

    def receiveMessages():
        mac = service.macAdress.get_mac_adress()[-5:]
        hostMACAddress = 'B8:27:EB:C9:'+mac
        print(hostMACAddress)
    
        port = 2
        backlog = 1
        size = 1024
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((hostMACAddress, port))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.settimeout(10)
        s.listen(backlog)
        os.system('sudo hciconfig hci0 piscan')
       # try:
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
                update_wifi("/home/admin/grow/GrowBox/src/service/wpa_supplicant.conf",name,password)
                fileRewrite()
                