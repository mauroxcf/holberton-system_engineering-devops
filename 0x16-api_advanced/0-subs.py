#!/usr/bin/python3
"""
0-main
"""
import requests as reqs
from sys import argv


def number_of_subscribers(subreddit):
    """ obtain number of subscribers"""
    if subreddit is None:
        return 0
    else:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {'user-agent': 'mauroxdev03'}
        response = reqs.get(url, headers=headers).json()
        subs_count = (response["data"]["subscribers"])
        return subs_count
