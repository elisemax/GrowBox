
import bluetooth
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
        port = 3
        backlog = 1
        size = 1024
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.bind((hostMACAddress, port))
       # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(backlog)
     #   bluetooth.advertise_service(s,'hui', '1e0ca4ea-299d-4335-93eb-27fcfe7fa848')
        os.system('sudo hciconfig hci0 piscan')
        try:
            print('started connecting')
            client, clientInfo = s.accept()
            while 1:
                print('waitong for bluetooth connection..')
                data = client.recv(size)
                if data:
                    print("Polu4ili data po bluetooth")
                    print(data)
                    client.send(data) # Echo back to client
                    client.send('Otpravili data nazad')
                    #interface = 'wlan0'
                    #name = ‘Wifi’
                    #password = ‘password’
                    #os.system('iwconfig ' + interface + ' essid ' + name + ' key ' + password)
        except:	
            print("Closing socket")
            client.close()
            s.close()