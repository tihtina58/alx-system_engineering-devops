#!/usr/bin/python3
"""
requesting data from an api
"""
import requests
from sys import argv


def show():
    """display data"""
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = user.get('name')
            break
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print(f'\t{task}')


if __name__ == '__main__':
    show()
