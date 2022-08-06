


from sensors.bluetoosh import Bluetoosh
from email import header
from email.utils import localtime
import requests
import JsonAdapter.adapter as ad
import time
import git



#systemGrow.idUpdate()
headers = {"Content-Type":"application/json", "Content-Length":"16","Host":"p5023.dev.inited.cz"}
while(True): 

    #try:  

    
        #systemGrow.connectToWifi()
    Bluetoosh.receiveMessages()
        
    systemGrow = ad.Adapter(True,True,True,True)
    
    #False, False, False, False
    #True,True,True,True
        
    
       
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
        
    #post = requests.post(url = 'http://p5023.dev.inited.cz/api/test/', json = {
    #"controlUnitId": systemGrow.controlUnitId,
    #"name": "Test",
    #"lightsRealStatus": systemGrow.ledStatus,
    #"temperature": systemGrow.temperature,
    #"pH": systemGrow.ph,
    #"humidity1": systemGrow.hum1,
    #"humidity2": systemGrow.hum2,
    #"humidity3": systemGrow.hum3,
    #"humidity4": systemGrow.hum4,
    #"ppm": systemGrow.ec },headers=headers)
    if(systemGrow.hum1==True or systemGrow.hum2==True or systemGrow.hum3 == True or systemGrow.hum4 == True or systemGrow.waterlevel == False):
        print("turning off pump")
        systemGrow.setPump(False)
    else:
        print("turning on pump")
        systemGrow.setPump(True)
    
    print("ec: ")
    print(systemGrow.ec)
    
    
    print("ph")
    print(systemGrow.ph)
    
    time.sleep(2)
   
   

        
        
    #except Exception:
    #    print(Exception)
    #    pass


        
