#!/usr/bin/python3
"""export user tasks data in JSON format."""
import json
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

    tasks_list = []
    data = {emp_id: tasks_list}

    for task in tasks:
        title = task.get('title')
        completed = task.get('completed')
        dic = {"task": title, "completed": completed, "username": emp_username}
        tasks_list.append(dic)

    with open("{}.json".format(emp_id), "w") as f:
        json.dump(data, f)
        f.close()
