


import requests
import JsonAdapter.adapter

r = requests.post('http://httpbin.org/post', json={"key": "value"})
#print(r.status_code)
systemGrow = JsonAdapter.adapter.Adapter()
#while(True):

systemGrow.get_ledStatus()
systemGrow.ledTurnOn()
print(systemGrow.get_ledStatus())


