
import bluetooth
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
    def receiveMessages():
        hostMACAddress = 'B8:27:EB:C9:EF:55' 
        port = 3
        backlog = 1
        size = 1024
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.bind((hostMACAddress, port))
        s.listen(backlog)
        try:
            client, clientInfo = s.accept()
            while 1:
                data = client.recv(size)
                if data:
                    print(data)
                    client.send(data) # Echo back to client
                    client.send('idi nahoi')
        except:	
            print("Closing socket")
            client.close()
            s.close()