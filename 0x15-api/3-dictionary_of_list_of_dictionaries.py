#!/usr/bin/python3
""" Export to CSV """
if __name__ == "__main__":
    import csv
    import requests
    import json

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    data = {}
    for user in users:
        payload = {'userId': user.get("id")}
        tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=payload).json()
        list_task = []
        for task in tasks:
            list_task.append({"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": user.get("username")})
        data[user.get("id")] = list_task
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
