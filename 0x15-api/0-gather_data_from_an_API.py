#!/usr/bin/python3
""" Consume Api"""
if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'userId': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()
    user_name = user.get('name')
    done = list(filter(lambda x: x.get("completed") is True, tasks))
    print("Employee {} is done with tasks({:d}/{:d}):".format(user_name,
          len(done), len(tasks)))
    for task_done in done:
        print("\t {}".format(task_done.get("title")))
