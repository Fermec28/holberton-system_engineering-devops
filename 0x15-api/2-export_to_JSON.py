#!/usr/bin/python3
""" Export to CSV """
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv
    import json

    payload = {'userId': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params=payload).json()
    list_task = []
    for task in tasks:
        list_task.append({"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": user.get("username")})
    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump({argv[1]: list_task}, f)
