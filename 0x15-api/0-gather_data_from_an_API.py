#!/usr/bin/python3
"""
This script fetches and displays task completion information
for a given employee from a JSONPlaceholder API.
"""

import sys
import requests

# Constants
BASE_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_api.py <employee_ID>",
              file=sys.stderr)
        sys.exit(1)

    employee_ID = sys.argv[1]

    try:
        user_response = requests.get(f"{BASE_URL}users/{employee_ID}",
                                     timeout=10)
        user_response.raise_for_status()
        user = user_response.json()
    except requests.RequestException as e:
        print(f"Error fetching user data: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        todo_response = requests.get(f"{BASE_URL}todos",
                                     params={"userId": employee_ID},
                                     timeout=10)
        todo_response.raise_for_status()
        todos = todo_response.json()
    except requests.RequestException as e:
        print(f"Error fetching todos: {e}", file=sys.stderr)
        sys.exit(1)

    done_tasks = [todo.get("title") for todo in todos if todo.get("completed")]
    num_of_done_tasks = len(done_tasks)
    num_of_all_tasks = len(todos)

    employee_name = user.get("name")
    print(f"Employee {employee_name}\
        is done with tasks({num_of_done_tasks}/{num_of_all_tasks}):")

    for done_task in done_tasks:
        print(f"\t {done_task}")
