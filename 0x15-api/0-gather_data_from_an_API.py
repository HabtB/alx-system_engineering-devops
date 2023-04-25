#!/usr/bin/python3
"""Makes a request to the REST API to get TODO list progress of employees"""

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
    number_of_completed_tasks = 0
    completed_tasks = []

    for task in tasks:
        if task['completed'] is True:
            completed_tasks.append(task)
            number_of_completed_tasks += 1

    """ Total Number of tasks """
    total_number_of_tasks = len(tasks)

    """ Print the employee TODO list progress """
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
          number_of_completed_tasks, total_number_of_tasks))

    """Print the title of completed tasks"""
    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    first_line(int(sys.argv[1]))
