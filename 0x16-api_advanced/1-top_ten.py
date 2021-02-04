#!/usr/bin/python3
"""
module to get the subscribers info
"""
import requests


def top_ten(subreddit):
    """ obtain number of subscribers
    - url: that we pass the subreddit.
    - headers: contain the user that
    thats its making the request.
    - make the request GET to the url
    and access key subscribers in the
    data key of the url.
    """
    if subreddit is None:
        return (0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'mauroxdev03'}
    limit = {'limit': '10'}
    response = requests.get(url, headers=headers, params=limit)
    for i in range(10):
        titles = response.json().get("data", {}).get("children", ())[i].get("data", {}).get("title", "")
        print(titles)
