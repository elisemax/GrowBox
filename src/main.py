


from sensors.bluetoosh import Bluetoosh
from email import header
from email.utils import localtime
import requests
import JsonAdapter.adapter as ad
import time
import git



#systemGrow = JsonAdapter.adapter.Adapter(False)

#systemGrow.idUpdate()
headers = {"Content-Type":"application/json", "Content-Length":"16","Host":"p5023.dev.inited.cz"}
while(True): 

    #try:  

    systemGrow = ad.Adapter(False)
        #systemGrow.connectToWifi()
        #Bluetoosh.receiveMessages(False)
        

        
        #tJsonObj = rGet.text

        #systemGrow.phUpdate()
        #systemGrow.Json_Upd()
        #systemGrow.temperatureUpdate()
        #time.sleep(3)
        #systemGrow.ledUpdateStatus(tJsonObj)
        #systemGrow.get_ledStatus()
        #systemGrow.tdsUpdate()
        #systemGrow.humUpdate()
        #systemGrow.phUpdate()# rGet = requests.get('http://192.168.0.10:8080/grow/status',json=systemGrow.Json_Obj())
        
        #systemGrow.getTime()
        
    time.sleep(3)
        #print(rGet.status_code)
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
        
    jsonObj = systemGrow.createJsonObj(systemGrow.controlUnitId, systemGrow.ledStatus, systemGrow.temperature, systemGrow.ph, systemGrow.ec, systemGrow.hum, "2022-07-23T13:21:37.000Z");
    print(jsonObj)
    post = requests.post(url = 'http://p5023.dev.inited.cz/api/test/', json = {"controlUnitId": systemGrow.controlUnitId,"name": "Test",    "lightsRealStatus": systemGrow.ledStatus,
    "temperature": systemGrow.temperature,
    "pH": systemGrow.ph,
    "humidity": systemGrow.humidity,
    "ppm": systemGrow.ec,
    "createdAt": "2022-07-23T15:29:20.000Z" },headers=headers)
        #jsonObj = systemGrow.createJsonObj("farm-2141", "true",22, 6, 400,     1,      "at",        )
    #r = requests.post(url = 'http://p5023.dev.inited.cz/api/test/' ,json = {"controlUnitId":"piton"},headers=headers)
        #print('http://p5023.dev.inited.cz/api/test/'+systemGrow.controlUnitId)
        #print(jsonObj)
    print(post.status_code)
   

        
        
    #except Exception:
    #    print(Exception)
    #    pass


        
