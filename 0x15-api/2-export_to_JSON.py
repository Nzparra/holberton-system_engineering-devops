#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, uid)
    name = requests.get(user).json().get('username')
    to_do = '{}todos?userId={}'.format(url, uid)
    jsn = requests.get(to_do).json()
    tasks = []
    for i in jsn:
        task = {"task": i.get('title'), "completed": i.get('completed'),
                "username": name}
        tasks.append(task)
    filename = '{}.json'.format(uid)
    with open(filename, mode='w') as file_json:
        json.dump({str(uid): tasks}, file_json)
