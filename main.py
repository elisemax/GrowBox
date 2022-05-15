



from email.utils import localtime
import requests
import JsonAdapter.adapter
import time
import git




systemGrow = JsonAdapter.adapter.Adapter()
systemGrow.idUpdate()
while(True): 
    try:  



        time.sleep(1)
        rGet = requests.get('http://192.168.0.10:8080/grow/status',json=systemGrow.Json_Obj())
        tJsonObj = rGet.text
        systemGrow.phUpdate()
        systemGrow.Json_Upd()
        systemGrow.temperatureUpdate()
        time.sleep(3)
        systemGrow.ledUpdateStatus(tJsonObj)
        systemGrow.get_ledStatus()
        systemGrow.tdsUpdate()
        systemGrow.humUpdate()
        systemGrow.phUpdate()
        systemGrow.getTime()
        #bluetooth.bluetooth.receiveMessages()
        #print(rGet.status_code)
        #g = git.cmd.Git('https://github.com/elisemax/GrowBox.git')
        #g.pull()
    
        
    except Exception:
        print(Exception)
        pass

     
        
