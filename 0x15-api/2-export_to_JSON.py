#!/usr/bin/python3
"""Makes a request to the REST API to get TODO list progress of employees"""
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + str(employee_id)
    response = requests.get(url)
    employee_data = response.json()

    """ Get the employee name and the number of completed tasks"""
    employee_name = employee_data['name']
    url2 = url + "/todos"
    response = requests.get(url2)
    tasks = response.json()

    print(tasks)

    task_dict = {employee_id: []}
    for task in tasks:
        task_dict[employee_id].append({
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_data['username']
            })

    """ Export data to JSON file """
    file_name = "{}.json".format(employee_id)
    with open(file_name, mode='w') as json_file:
        json.dump(task_dict, json_file)
