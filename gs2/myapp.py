import requests
import json


URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name':"sonam",
    'roll':101,
    'city':"ranchi"
}
# client → server 
json_data = json.dumps(data)#json.dumps() is used on your side (to CREATE JSON).Python → JSON string
r = requests.post(url=URL, data=json_data)#you send this JSON string in the HTTP POST
# server → client
data = r.json()#r.json() is used on the API response side (to READ JSON).JSON → Python
print(data)