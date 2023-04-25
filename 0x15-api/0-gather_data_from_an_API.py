import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line(id):
    """ Fetch number of tasks """

    todos_count = 0
    todos_done = 0

    resp = requests.get(todos_url).json()
    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1

    employee_name = None
    completed_tasks = []
    total_number_of_tasks = 0
    number_of_completed_tasks = 0

    url = f"{users_url}/{id}"
    employee_data = requests.get(url).json()
    employee_name = employee_data['name']

    url2 = f"{users_url}/{id}/todos"
    tasks = requests.get(url2).json()
    for task in tasks:
        if task['completed'] is True:
            completed_tasks.append(task)
            number_of_completed_tasks += 1
        total_number_of_tasks += 1

    """ Print the employee TODO list progress """
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
          number_of_completed_tasks, total_number_of_tasks))

    """Print the title of completed tasks"""
    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    first_line(int(sys.argv[1]))
