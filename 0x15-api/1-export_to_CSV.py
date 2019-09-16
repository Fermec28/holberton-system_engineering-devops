#!/usr/bin/python3
""" Export to CSV """
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(argv[1])).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), 'w') as writeFile:
        writer = csv.writer(writeFile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([argv[1], user.get("username"),
                             task.get("completed"), task.get("title")])
