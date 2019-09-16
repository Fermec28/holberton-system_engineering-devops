#!/usr/bin/python3
""" Export to CSV """
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    payload = {'userId': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    user = user.json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params=payload)
    with open('{}.csv'.format(argv[1]), 'w') as writeFile:
        writer = csv.writer(writeFile, quoting=csv.QUOTE_ALL)
        for task in tasks.json():
            row = []
            row.append(argv[1])
            row.append(user.get("username"))
            row.append(task.get("completed"))
            row.append(task.get("title"))
            writer.writerow(row)
