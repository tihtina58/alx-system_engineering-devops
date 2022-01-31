#!/usr/bin/python3
"""prints information about employee and his/her tasks using employee id."""
import requests
from sys import argv

if __name__ == '__main__':
    emp_id = argv[1]
    route = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r = requests.get(route)
    usr_info = r.json()
    emp_name = usr_info.get('name')

    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    route = url.format(emp_id)
    r = requests.get(route)
    tasks = r.json()

    done_tasks = 0
    for task in tasks:
        if task.get('completed') is True:
            done_tasks += 1

    tot_tasks = len(tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, done_tasks, tot_tasks))

    for task in tasks:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
