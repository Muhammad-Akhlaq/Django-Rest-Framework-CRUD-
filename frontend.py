#python 3rd party app to get data from Django Rest Framework

import requests
import json
#to get 1 student data
def get_one_data():
    URL = "http://127.0.0.1:8000/student_info/2"
    r = requests.get(url = URL)
    data = r.json()
    for i in range(5):
        print(data['name'])
    print(data)

#to get all student data
def get_all_data():
    URL = "http://127.0.0.1:8000/student_info/"
    r = requests.get(url = URL)
    data = r.json()
    print(data)

#to send 1 student data for creation
def create():
    URL = "http://127.0.0.1:8000/student_create/"
    data = {'name':'rizwan','roll':3,'city':'gadyala'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    #response msg
    data = r.json()
    print(data)


#to send student data for update
def update():
    URL = "http://127.0.0.1:8000/student_update/"
    data = {'name':'rizwan','roll':4,'city':'Daska'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    #response msg
    data = r.json()
    print(data)


#to send student data for update
def delete():
    URL = "http://127.0.0.1:8000/student_delete/"
    data = {'name':'rizwan'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    #response msg
    data = r.json()
    print(data)


#to check field validation
def check_field_validation():
    URL = "http://127.0.0.1:8000/student_create/"
    data = {'name':'rizwan','roll':201,'city':'gadyala'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    #response msg
    data = r.json()
    print(data)


#to check object validation
def check_object_validation():
    URL = "http://127.0.0.1:8000/student_create/"
    data = {'name':'Akhlaq','roll':1,'city':'daska'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    #response msg
    data = r.json()
    print(data)

#to check validation
def check_validation():
    URL = "http://127.0.0.1:8000/student_create/"
    data = {'name':'rizwan','roll':1,'city':'daska'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    #response msg
    data = r.json()
    print(data)


#to check api_view(browserable api)
def check_api_view():
    URL = "http://127.0.0.1:8000/hello/"
    r = requests.get(url = URL)
    data = r.json()
    print('GET')
    print(data['print'])
    print('POST')
    data = {'name':'rizwan'}
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url = URL, headers = headers, data = json_data)
    #response msg
    data = r.json()
    print(data)
#check_api_view()


#to get student data
def get_student(id):
    URL = "http://127.0.0.1:8000/student_info/"
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
get_student(2)
get_student()