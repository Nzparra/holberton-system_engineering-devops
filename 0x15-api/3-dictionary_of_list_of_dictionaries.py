#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import json
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    data = requests.get(user).json()
    tasks = {}
    for user in data:
        name = user.get('username')
        uid = user.get('id')
        to_dos = '{}todos?userId={}'.format(url, uid)
        task = requests.get(to_dos).json()
        f_task = []
        for i in task:
            dict_task = {"username": name,
                         "task": i.get('title'),
                         "completed": i.get('completed')}
            f_task.append(dict_task)
        tasks[str(uid)] = f_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file_data:
        json.dump(tasks, file_data)
