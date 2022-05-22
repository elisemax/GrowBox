



from email import header
from email.utils import localtime
import requests
import JsonAdapter.adapter
import time
import git




systemGrow = JsonAdapter.adapter.Adapter()
systemGrow.idUpdate()
headers = {"accept":"application/json","Content-Type":"application/json;"}
while(True): 
    #try:  

        time.sleep(1)
        
        #tJsonObj = rGet.text
        

        systemGrow.phUpdate()
        systemGrow.Json_Upd()
        systemGrow.temperatureUpdate()
        time.sleep(3)
        #systemGrow.ledUpdateStatus(tJsonObj)
        systemGrow.get_ledStatus()
        systemGrow.tdsUpdate()
        systemGrow.humUpdate()
        systemGrow.phUpdate()
        #rGet = requests.get('http://192.168.0.10:8080/grow/status',json=systemGrow.Json_Obj())
        jsonObj = systemGrow.createJsonObj(systemGrow.controlUnitId,systemGrow.get_ledStatus(),systemGrow.temperature,systemGrow.ph,systemGrow.ec,systemGrow.getTime())
        #systemGrow.getTime()
        #bluetooth.bluetooth.receiveMessages()
        #print(rGet.status_code)
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
        rPut = requests.put('https://p5023.dev.inited.cz/api/test/'+systemGrow.controlUnitId,json=jsonObj,headers=headers)
        
    #except Exception:
    #    print(Exception)
    #    pass


        
