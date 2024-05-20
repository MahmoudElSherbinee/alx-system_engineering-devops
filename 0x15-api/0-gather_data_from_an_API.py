#!/usr/bin/python3
"""
 a Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_ID = sys.argv[1]
    userResponse = requests.get(url + "users/" + employee_ID).json()

    params = {"userId": employee_ID}
    todoResponse = requests.get(url + "todos", params=params).json()

    done_tasks = []
    num_of_done_tasks = 0
    num_of_all_tasks = 0
    for todo in todoResponse:
        if todo.get("completed") is True:
            done_tasks.append(todo.get("title"))
            num_of_done_tasks += 1
        num_of_all_tasks += 1

    employee_name = userResponse.get("name")
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          num_of_done_tasks,
                                                          num_of_all_tasks))

    for done_task in done_tasks:
        print("\t {}".format(done_task))
