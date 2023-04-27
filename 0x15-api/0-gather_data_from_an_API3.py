#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
from sys import argv


if __name__ == '__main__':
    e_Id = argv[1]
    url = "https://jsonplaceholder.typicode.com/" + "users/{}".format(e_Id)
    response = requests.get(url)
    employeeName = response.json().get('name')

    payload = {"userId": e_Id}
    url2 = url + '/todos/'
    tasks = requests.get(url2, params=payload).json()

    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
