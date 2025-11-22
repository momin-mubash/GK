import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    #params means query parameters — the small data you send after a ? in a URL.
    params = {}

    if id is not None:
        params['id'] = id

    r = requests.get(URL, params=params)
    print(r.json())


# Call without ID → get list of all students
#get_data()

# Call with ID → get a single student
# get_data(1)


#create data and posting it on the server
def post_data():
    data = {
        'name' : 'Ravi',
        'roll' : 104,
        'city' : 'Mumbai'
    }
    json_data = json.dumps(data)

    r = requests.post(url=URL, data=json_data)
    print(r.json())
#post_data()


#update data and posting it on the server
