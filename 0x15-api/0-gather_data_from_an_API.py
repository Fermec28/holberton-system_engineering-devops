#!/usr/bin/python3
""" Consume Api"""
if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'userId': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    user_name = user.json()['name']
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                     params=payload)
    done = list(filter(lambda x: x["completed"] is True, tasks.json()))
    print("Employee {} is done with tasks({}/{}):".format(user_name,
          len(done), len(tasks.json())))
    for task_done in done:
        print("\t{}".format(task_done["title"]))
