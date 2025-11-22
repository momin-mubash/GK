import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    #params means query parameters — the small data you send after a ? in a URL.
    params = {}

    if id is not None:
        params['id'] = id

    r = requests.get(URL, params=params)
    print(r.json())


# Call without ID → get list of all students
get_data()

# Call with ID → get a single student
# get_data(1)
