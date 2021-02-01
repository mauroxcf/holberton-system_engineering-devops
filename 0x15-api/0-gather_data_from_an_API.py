#!/usr/bin/python3
# script that, using REST API, for a given employee ID, returns information
""" USING A REST API """


import requests


if __name__ == '__main__':
    import requests as reqs
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    sesion = reqs.Session()  # open a session to do multiple query

    comp_task = []
    response = sesion.get(url)  # we got a list of task with other info
    response2 = sesion.get(url2)  # we get a list of task with name_employee
    task_list = response.json()  # convert the obtain info into json
    name = response2.json()["name"]  # convert the obtain name info into json

    for task in task_list:
        if task["completed"]:  # if the task completed its true
            comp_task.append(task["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(comp_task), len(task_list)))
    for i in comp_task:
        print("\t " + i)
