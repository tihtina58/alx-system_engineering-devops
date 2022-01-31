#!/usr/bin/python3
"""export user tasks data to CSV format."""
import requests
from sys import argv

if __name__ == '__main__':
    emp_id = argv[1]
    route = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r = requests.get(route)
    usr_info = r.json()
    emp_username = usr_info.get('username')

    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    route = url.format(emp_id)
    r = requests.get(route)
    tasks = r.json()

    with open("{}.csv".format(emp_id), "w") as f:
        for task in tasks:
            task_status = task.get('completed')
            task_title = task.get('title')
            string = '"{}","{}","{}","{}"\n'.format(emp_id, emp_username,
                                                    task_status, task_title)
            f.write(string)
        f.close()
