


from sensors.bluetoosh import Bluetoosh
from email import header
from email.utils import localtime
import requests
import JsonAdapter.adapter as ad
import time
import git
import datetime
import os



#systemGrow.idUpdate()

#while(True): 

   # try:  

    
        #systemGrow.connectToWifi()
    
    
    #False, False, False, False
    #True,True,True,True
        
    
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
headers = {"Content-Type":"application/json", "Content-Length":"16","Host":"p5023.dev.inited.cz"}
systemGrow = ad.Adapter(True, True, True, True)


datetime_object = datetime.datetime.now()
dateString = str(datetime_object)[:-4]
print(dateString)
response = requests.post(url = 'http://p5023.dev.inited.cz/api/test/', json = {
"controlUnitId": systemGrow.controlUnitId,
"name": "AugustFarm",
"temperature": systemGrow.temperature,
"pH": systemGrow.ph,
"humidity1": systemGrow.hum1,
"humidity2": systemGrow.hum2,
"humidity3": systemGrow.hum3,
"humidity4": systemGrow.hum4,
"ppm": systemGrow.ec
}, headers=headers),


#Led.ledControl(response)
print('ph:')
print(systemGrow.ph)

print('ec')
print(systemGrow.ec)
    
Bluetoosh.receiveMessages()
            
if (systemGrow.hum1==True or systemGrow.hum2==True or systemGrow.hum3 == True or systemGrow.hum4 == True or systemGrow.waterlevel == False):
    print("turning off pump")
    systemGrow.setPump(False)
else:
    print("turning on pump")
    systemGrow.setPump(True)
        
    print("ec: ")
    print(systemGrow.ec)
    print(systemGrow.controlUnitId)
        
    print("ph")
    print(systemGrow.ph)
    
    
txt_log = "ec = "+ systemGrow.ec + "ph = " + systemGrow.ph
os.system('echo ' + txt_log + ' >> /home/frm04/crontest.txt')
            
        
        
   # except Exception as e:
   #         print(e)
   #         pass
   
   

        
        
    #except Exception:
    #    print(Exception)
    #    pass


        
