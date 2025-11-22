import requests
URL = "http://127.0.0.1:8000/stuinfo/"

r = requests.get(url=URL)#the response is not raw JSON.

#It is a Response object, and inside it, the body is stored as a string, like:
#"[{\"id\": 1, \"name\": \"Momin\"}]"
#This is a JSON string, not a Python datatype.

data = r.json()
#.json() converts that string into Python dictionary or list so you can actually work with it.
print(data)
print(type(data))