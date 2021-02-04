#!/usr/bin/python3
"""
module to get the subscribers info
"""
import requests


def number_of_subscribers(subreddit):
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

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'mauroxdev03'}
    response = requests.get(url, headers=headers)
    subs_count = response.json().get('data', {}).get("subscribers", 0)
    return subs_count
