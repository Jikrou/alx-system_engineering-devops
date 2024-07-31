#!/usr/bin/python3

""" a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS)}:")
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    employee_rsp = requests.get(f"{base_url}/users/{employee_id}").json()
    EMPLOYEE_NAME = employee_rsp['name']

    TOTAL_NUMBER_OF_TASKS = requests.get(
            f"{base_url}/users/{employee_id}/todos").json()

    NUMBER_OF_DONE_TASKS = sum(
            1 for t in TOTAL_NUMBER_OF_TASKS if t['completed'])

    print(
            "Employee"
            f" {EMPLOYEE_NAME} is done with tasks("
            f"{NUMBER_OF_DONE_TASKS}/{len(TOTAL_NUMBER_OF_TASKS)}):")

    for t in TOTAL_NUMBER_OF_TASKS:
        if t['completed']:
            print(f"\t{t['title']}")
