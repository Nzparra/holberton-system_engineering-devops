#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, argv[1])
    jsn = requests.get(user).json()
    print("Employee {} is done with tasks".format(jsn.get('name')), end="")
    to_do = '{}todos?userId={}'.format(url, argv[1])
    jsn = requests.get(to_do).json()
    tasks = []
    for i in jsn:
        if i.get('completed'):
            tasks.append(i)
    print("({}/{}):".format(len(tasks), len(jsn)))
    for i in tasks:
        print("\t {}".format(i.get("title")))
