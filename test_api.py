import json
import requests

host = 'http://localhost:8000/api'

header = {"Content-Type": "application/json"}


def test_create_users():

    data = {
        "name": "2222 Jone",
        "email": "b32sh@gmail.com",
        "citizen_id": "3333967890123",
        "gender": 2,
        "address": {
            "house_number": "222/3",
            "village": "sompong village",
            "road": "suppasarn",
            "sub_district": "paknam",
            "district": "meuang",
            "province": "bkk",
            "zip_code": "12912",
        }
    }

    response = requests.post(url=f'{host}/users/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_list_users():
    response = requests.get(url=f'{host}/users/', headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


def test_update_users(pk):

    data = {
        "name": "Beth dda",
        "email": "beth@gmail.com",
        "citizen_id": "1399997890123",
        "gender": 1,
        "address": {
            'house_number': '222/3',
            'village': 'sompong village',
            'road': 'suppasarn',
            'sub_district': 'paknam',
            'district': 'meuang',
            'province': 'bkk',
            'zip_code': '33333',
        }
    }

    response = requests.put(url=f'{host}/users/{pk}/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_retrieve_user(pk):
    
    response = requests.get(url=f'{host}/users/{pk}/', headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_patch_user(pk):

    data = {
        # "name": "Beth dda",
        # "email": "beth@gmail.com",
        "citizen_id": "6666666333366",
        # "gender": 1,
        "address": {
            'house_number': '111/1',
            'village': 'sompong village',
            'road': 'suppasarn',
            'sub_district': 'paknam',
            'district': 'meuang',
            'province': 'krabi',
            'zip_code': '33333',
        }
    }
    response = requests.patch(url=f'{host}/users/{pk}/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")
    
def test_delete_user(pk):
    
    response = requests.delete(url=f'{host}/users/{pk}/')
    print(f"\nstatus {response.status_code}")

if __name__ == '__main__':

    # test_create_users()
    # test_list_users()
    test_update_users(8)
    # test_retrieve_user(1)
    # test_patch_user(1)
    # test_delete_user(7)
    