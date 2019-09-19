#!/usr/bin/python3
import requests
"""count number of subscribers"""


def recurse(subreddit, hot_list=[], after=None):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Fermec28'}
    payload = {"after": after}
    try:
        result = requests.get(url, headers=headers, params=payload,
                              allow_redirects=False).json()
    except:
        return(None)
    if ("data" in result and "children" in result.get("data")):
        for post in result.get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        if "after" in result.get("data") and result.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           result.get("data").get("after"))
        else:
            return hot_list
    else:
        return(None)
