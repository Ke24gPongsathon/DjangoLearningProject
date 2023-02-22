import json
import requests

host = 'http://localhost:8000/api'

header = {"Content-Type": "application/json"}


def test_list_users():
    # data = {"first_name": "Beth",
    #         "last_name": "Jones",
    #         "subject_title": "Coding",
    #         "score": 100
    #         }

    response = requests.get(url=f'{host}/users/', headers=header,)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_get_user():
    # data = {"first_name": "Beth",
    #         "last_name": "Jones",
    #         "subject_title": "Coding",
    #         "score": 100
    #         }

    response = requests.post(url=f'{host}/student_score/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")



if __name__ == '__main__':

    test_list_users()