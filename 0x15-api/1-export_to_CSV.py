#!/usr/bin/python3
"""Makes a request to the REST API to get TODO list progress of employees"""

import requests
import sys
import csv

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
    number_of_completed_tasks = 0
    completed_tasks = []

    for task in tasks:
        if task['completed'] is True:
            completed_tasks.append(task)
            number_of_completed_tasks += 1

    """ Export data to CSV file """
    file_name = "{}.csv".format(employee_id)
    with open(file_name, mode='w') as csv_file:
        for task in tasks:
            csv_file.write('"{}", "{}", "{}", "{}"\n'.format(employee_id,
                           employee_name, task['completed'], task['title']))
