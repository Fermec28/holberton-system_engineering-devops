#!/usr/bin/python3
import requests
"""count number of subscribers"""


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Fermec28'}
    try:
        subreddit = requests.get(url, headers=headers,
                                 allow_redirects=False).json()
    except:
        return 0
    if ("data" in subreddit and "subscribers" in subreddit.get("data")):
        return subreddit.get("data").get("subscribers")
    else:
        return 0
