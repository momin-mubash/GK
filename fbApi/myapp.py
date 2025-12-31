import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    #params means query parameters — the small data you send after a ? in a URL.
    params = {}

    if id is not None:
        params['id'] = id
    headers = {'content-Type' : 'application/json'}
    r = requests.get(URL, headers = headers ,  params=params)
    print(r.json())


# Call without ID → get list of all students
get_data()

# Call with ID → get a single student
# get_data(1)


#create data and posting it on the server
def post_data():
    data = {
        'roll' : 129, 
        'name' :'khizar',
        'city' : 'karnataka'
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)

    r = requests.post(url=URL,headers=headers ,data=json_data)
    print(r.json())
post_data()


#update data and posting it on the server
def update_data():
    data = {
        'roll' : 104, 
        'name' :'zohra',
        'city' : 'madina'
    }
    json_data = json.dumps(data)

    r = requests.put(url=URL, data=json_data)

    print(r.json())

#update_data()

#Delete
def delete_data():
    data = {
        'roll' : 150
    }
    json_data = json.dumps(data)

    r = requests.delete(url=URL, data=json_data)

    print(r.json())

#delete_data()
