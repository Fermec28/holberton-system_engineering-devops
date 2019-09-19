#!/usr/bin/python3
import requests
"""count number of subscribers"""


def top_ten(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Fermec28'}
    payload = {'limit': 10}
    try:
        result = requests.get(url, headers=headers, params=payload,
                              allow_redirects=False).json()
    except:
        return None
    if ("data" in result and "children" in result.get("data")):
        for post in result.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        return None
