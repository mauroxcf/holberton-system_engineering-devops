#!/usr/bin/python3
# script that, using REST API, for a given employee ID, returns information
""" USING A REST API """


if __name__ == '__main__':
    import csv
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
    name = response2.json()["username"]  # convert the obtain Uname into json

    for task in task_list:
        """ if task["completed"]:  # if the task completed its true """
        comp_task.append([id, name, task["completed"], task["title"]])

    with open("{}.csv".format(id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(comp_task)
