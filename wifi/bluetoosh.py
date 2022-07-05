
import socket
import os
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
        try:
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
                    client.send(data) # Echo back to client
                    #print('Otpravili data nazad')
                    # os.system('sed -c -i "s/\($TARGET_KEY *= *\).*/\1$REPLACEMENT_VALUE/" $CONFIG_FILE')
                    #interface = 'wlan0'
                    #name = ‘Wifi’
                    #password = ‘password’
                    #os.system('iwconfig ' + interface + ' essid ' + name + ' key ' + password)
                    parts = decoded.split(',')
                    interface = 'wlan0'
                    name = parts[0]
                    password = parts[1]
                    print(name)
                    print(password)
                    os.system('sudo iwconfig ' + interface + ' essid ' + name + ' key ' + password)
                    # os.system('sed -c -i "s/\($ssid *= *\).*/\1$name/" $wpa_supplicant.conf')
                    # os.system('sed -c -i "s/\($psk *= *\).*/\1$password/" $wpa_supplicant.conf')
                    # os.system('sed -c -i "s/\($key_mgmt *= *\).*/\1$WPA-PSK/" $wpa_supplicant.conf')
                    # os.system('reboot')

            
        except Exception as e :	
            print("Closing socket")
            print(e)
            client.close()
            s.close()