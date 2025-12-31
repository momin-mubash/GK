import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(roll=None):
    #params means query parameters — the small data you send after a ? in a URL.
    params = {}

    if roll is not None:
        params['roll'] = roll
    headers = {'content-Type' : 'application/json'}
    r = requests.get(URL, headers = headers ,  params=params)
    print(r.json())



# Call without ID → get list of all students
# get_data()

# Call with ID → get a single student
# get_data(103)


#create data and posting it on the server
def post_data():
    data = {
        'roll' : 104, 
        'name' :'sumit',
        'city' : 'kanpur',
        }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)

    r = requests.post(url=URL,headers=headers ,data=json_data)
    print(r.json())
# post_data()


#update data and posting it on the server
def update_data():
    data = {
        'id':2,
        'roll' : 102, 
        'name' :'zaid',
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)

    r = requests.put(url=URL,headers=headers, data=json_data)

    print(r.json())

# update_data()

#Delete
def delete_data():
    data = {
        'id' : 4
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)

    r = requests.delete(url=URL,headers=headers, data=json_data)

    print(r.json())

delete_data()
