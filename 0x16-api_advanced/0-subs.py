#!/usr/bin/python3
"""
module to get the subscribers info
"""
import requests as reqs


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
    else:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {'user-agent': 'mauroxdev03'}
        response = reqs.get(url, headers=headers, allow_redirect=False).json()
        subs_count = (response["data"]["subscribers"])
        return subs_count
