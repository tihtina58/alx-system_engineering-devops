#!/usrbin/python3

"""
This module gets the todo of a user identified by id
gotten from the api https://jsonplaceholder.typicode.com/users
"""

import requests
import sys

if __name__ == '__main__':
    userid = int(sys.argv[1])
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(userid))
    name = resp.json()['name']
    task_resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(userid))
    c_task = 0
    task_json = task_resp.json()
    t_len = len(task_json)
    completed_task_str = ''
    for i in task_json:
        if i['completed']:
            c_task += 1
            completed_task_str += ('\t{}\n'.format(i['title']))
    print('Employee {} is done with tasks({}/{}):'.format(name, c_task, t_len))
    print(completed_task_str)
