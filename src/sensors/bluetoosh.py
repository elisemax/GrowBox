
from calendar import c
import socket
import os
import sys
#conf_path = os.getcwd()
#sys.path.append(conf_path)
#sys.path.append(conf_path + '/home/admin/.local/lib/python3.9/') 
import time
from wifiUpdate import update_wifi
from configRewrite import fileRewrite


class Bluetoosh:
# def receiveMessages():
#   server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
#   port = 1
#   server_sock.bind(("",port))
#   server_sock.listen(1)
#   server_sock
  
  
#   client_sock,address = server_sock.accept()
#   print ("Accepted connection from " + str(address))
  
#   data = client_sock.recv(1024)
#   print ("received [%s]" % data)
  
#   client_sock.close()
#   server_sock.close()
    def receiveMessages(self):
        hostMACAddress = 'B8:27:EB:C9:EF:55'
        port = 2
        backlog = 1
        size = 1024
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.bind((hostMACAddress, port))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(backlog)
        #bluetooth.advertise_service(s,'hui', '1e0ca4ea-299d-4335-93eb-27fcfe7fa848')
        os.system('sudo hciconfig hci0 piscan')
       # try:
        print('started connecting')
        client, adress = s.accept()
        print('client accepted')
        while 1:
            print('waitong for data...')
            data = client.recv(size)
            print('data was get')
            if (data):
                print("Polu4ili data po bluetooth")
                print(data)
                decoded = data.decode('utf-8')
                parts = decoded.split(',')
                interface = 'wlan0'
                name = parts[0]
                password = parts[1]
                print(name)
                print(password)
                update_wifi.update_wifi("/home/admin/grow/GrowBox/src/service/wpa_supplicant.conf")
                fileRewrite.fileRewrite()
                