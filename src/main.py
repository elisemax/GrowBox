


from sensors.bluetoosh import Bluetoosh
from email import header
from email.utils import localtime
import requests
import JsonAdapter.adapter as ad
import time
import git



#systemGrow = JsonAdapter.adapter.Adapter(False)
# systemGrow.idUpdate()

while(True): 
    headers = {"Content-Type":"application/json", "Content-Length":350,"Host":"gkjtigt-fgbg-gbgb"}
    #try:  

        #systemGrow = ad.Adapter(False)
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
        
        
        #systemGrow.controlUnitId,
        #systemGrow.getLightsRealStatus,
        #systemGrow.getTemperature,systemGrow.getPH,
        #systemGrow.getPPM,systemGrow.getHum,
        #systemGrow.getTime)
        #jsonObj = systemGrow.createJsonObj("farm-2141", "true",22, 6, 400,     1,      "at",        )
    rPut = requests.post(url = 'http://p5023.dev.inited.cz/api/test/' ,data = {"controlUnitId":"piton"},headers=headers)
        #print('http://p5023.dev.inited.cz/api/test/'+systemGrow.controlUnitId)
        #print(jsonObj)
    print(str(rPut.json))

        
        
    #except Exception:
    #    print(Exception)
    #    pass


        
