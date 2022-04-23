



from email.utils import localtime
import requests
import JsonAdapter.adapter
import time


systemGrow = JsonAdapter.adapter.Adapter()
while(True):   
    #localtime = time.localtime()
    #result = time.strftime("%H:%M:%S",localtime)
    #print(result)
    time.sleep(1)
    rGet = requests.get('http://192.168.0.10:8080/grow/status',json=systemGrow.Json_Obj())
    timerJsonObj = rGet.text
    systemGrow.ledTimerControl(timerJsonObj)
    systemGrow.phUpdate()
    systemGrow.ledUpdateStatus()
    systemGrow.Json_Upd()
    systemGrow.ledTurnOn()
    time.sleep(5)
    systemGrow.ledTurnOff()
    print(rGet.status_code)
    
