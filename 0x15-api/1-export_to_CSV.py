#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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
        tasks.append([uid, name, i.get('completed'), i.get('title')])
    filename = '{}.csv'.format(uid)
    with open(filename, mode='w') as csv_employee:
        employee_writer = csv.writer(csv_employee,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for i in tasks:
            employee_writer.writerow(i)
