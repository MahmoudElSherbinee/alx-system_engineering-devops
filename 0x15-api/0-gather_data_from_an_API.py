import requests
import sys

# Employee EMPLOYEE_NAME is done with tasks
# (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
# TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_ID = sys.argv[1]
    userResponse = requests.get(url + "users/" + employee_ID)

    user = userResponse.json()

    params = {"userId": employee_ID}
    todoResponse = requests.get(url + "todos", params=params)

    todos = todoResponse.json()

    done_tasks = []
    num_of_done_tasks = 0
    num_of_all_tasks = 0
    for todo in todos:
        if todo.get("completed") is True:
            done_tasks.append(todo.get("title"))
            num_of_done_tasks += 1
        num_of_all_tasks += 1

    employee_name = user.get("name")
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          num_of_done_tasks,
                                                          num_of_all_tasks))

    for done_task in done_tasks:
        print("\t {}".format(done_task))
