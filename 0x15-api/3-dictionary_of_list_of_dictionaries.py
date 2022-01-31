#!/usr/bin/python3
"""export users tasks data in JSON format."""
import json
import requests

if __name__ == '__main__':
    route = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(route)
    users = r.json()

    data = {}
    for user in users:
        uid = user.get('id')
        uuname = user.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}/todos"
        route = url.format(uid)
        r = requests.get(route)
        tasks = r.json()

        tasks_list = []
        data[uid] = tasks_list

        for task in tasks:
            title = task.get('title')
            completed = task.get('completed')
            dic = {"task": title, "completed": completed, "username": uuname}
            tasks_list.append(dic)

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
        f.close()
