


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
        #Bluetoosh.receiveMessages(False)
        
    systemGrow = ad.Adapter( False, False,True, True)
        
    
       
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
        
    #jsonObj = systemGrow.createJsonObj(systemGrow.controlUnitId, systemGrow.ledStatus, systemGrow.temperature, systemGrow.ph, systemGrow.ec, systemGrow.hum, "2022-07-23T13:21:37.000Z");
    #print(jsonObj)
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
    
    print("ppm: ")
    print(systemGrow.ec)
    
    
    print("ph")
    print(systemGrow.ph)
    
    time.sleep(2)
   
   

        
        
    #except Exception:
    #    print(Exception)
    #    pass


        
