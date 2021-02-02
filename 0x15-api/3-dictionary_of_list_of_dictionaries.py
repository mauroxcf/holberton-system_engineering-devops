#!/usr/bin/python3
# script that, using REST API, for a given employee ID, returns information
""" USING A REST API """


if __name__ == '__main__':
    import json
    import requests as reqs
    from sys import argv

    sesion = reqs.Session()  # open a session to do multiple query

    json_string = {}
    user_list = []
    url2 = 'https://jsonplaceholder.typicode.com/users/'
    response2 = sesion.get(url2)  # we get all information about employees
    user_list = response2.json()

    for object in user_list:
        id = str(object["id"])  # obtain id of each employee
        username = object["username"]  # obtain username of each employee

        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

        response = sesion.get(url)  # we got a list of task with other info

        comp_task = []
        task_list = response.json()  # convert the obtain info into json

        for task in task_list:
            comp_task.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            })

        json_string.update({id: comp_task})  # dictionary with all the info
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_string, json_file)  # write a json file in json string
