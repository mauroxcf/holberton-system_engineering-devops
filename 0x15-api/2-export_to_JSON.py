#!/usr/bin/python3
# script that, using REST API, for a given employee ID, returns information
""" USING A REST API """


if __name__ == '__main__':
    import json
    import requests as reqs
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    sesion = reqs.Session()  # open a session to do multiple query

    json_string = {}
    comp_task = []
    task_value = {}
    response = sesion.get(url)  # we got a list of task with other info
    response2 = sesion.get(url2)  # we get a list of task with name_employee
    task_list = response.json()  # convert the obtain info into json
    name = response2.json()["username"]

    for task in task_list:
        comp_task.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": name
        })

    json_string.update({id: comp_task})
    with open('{}.json'.format(id), 'w') as json_file:
        json.dump(json_string, json_file)
