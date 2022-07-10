


from sensors.bluetoosh import Bluetoosh
from email import header
from email.utils import localtime
import requests
import JsonAdapter.adapter as ad
import time
import git



#systemGrow = JsonAdapter.adapter.Adapter(False)
#systemGrow.idUpdate()
headers = {"accept":"application/json","Content-Type":"application/json;"}
while(True): 
    #try:  

        #systemGrow = ad.Adapter(False)
        #systemGrow.connectToWifi()
        Bluetoosh.receiveMessages(False)
        

        
        #tJsonObj = rGet.text

        #systemGrow.phUpdate()
        #systemGrow.Json_Upd()
        #systemGrow.temperatureUpdate()
        #time.sleep(3)
        #systemGrow.ledUpdateStatus(tJsonObj)
        #systemGrow.get_ledStatus()
        #systemGrow.tdsUpdate()
        #systemGrow.humUpdate()
        #systemGrow.phUpdate()
        #rGet = requests.get('http://192.168.0.10:8080/grow/status',json=systemGrow.Json_Obj())
        
        #systemGrow.getTime()
        
        time.sleep(5)
        #print(rGet.status_code)
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
        
        #jsonObj = systemGrow.createJsonObj(systemGrow.controlUnitId,
        #systemGrow.getLightsRealStatus,
        #systemGrow.getTemperature,systemGrow.getPH,
        #systemGrow.getPPM,systemGrow.getHum,
        #systemGrow.getTime
        #rPut = requests.post('http://p5023.dev.inited.cz/api/test/',data=jsonObj,headers=headers)
        #print('http://p5023.dev.inited.cz/api/test/'+systemGrow.controlUnitId)
        #print(jsonObj)
        #print(str(rPut.json))

        
        
    #except Exception:
    #    print(Exception)
    #    pass


        
