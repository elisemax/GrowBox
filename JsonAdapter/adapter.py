import json 

class Adapter:
    def __init__(self,pathJson):
        with open(pathJson) as json_file:
            data = json.load(json_file)
