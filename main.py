



from email.utils import localtime
import requests
import JsonAdapter.adapter
import time


systemGrow = JsonAdapter.adapter.Adapter()
while(True): 
    try:  
        #localtime = time.localtime()
        #result = time.strftime("%H:%M:%S",localtime)
        #print(result)
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
        print(rGet.status_code)
    except Exception:
        pass

     
        
