#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 gather_data_from_an_API.py employee_id")
    sys.exit(1)

employee_id = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

response = requests.get("https://jsonplaceholder.typicode.com/users/"
                        + str(employee_id))
employee_data = response.json()
employee_name = employee_data['name']

response = requests.get(url)
if response.status_code != 200:
    print('Error: API request unsuccessful.')
    sys.exit(1)

todos = response.json()
total_tasks = len(todos)
done_tasks = sum(todo.get('completed') for todo in todos)

print('Employee {} is done with tasks({}/{}):'.
      format(employee_name, done_tasks, total_tasks))
for todo in todos:
    if todo.get('completed'):
        print('\t {}'.format(todo.get('title')))
