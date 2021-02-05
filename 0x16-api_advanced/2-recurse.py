#!/usr/bin/python3
"""
module to get the hot titles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ obtain number of hot titles
    - url: that we pass the subreddit.
    - headers: contain the user that
    thats its making the request.
    - make the request GET to the url
    and access key titles in the
    data key of the url.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'mauroxdev03'}
    after2 = {'after': after}
    response = requests.get(
        url, headers=headers, params=after2,
        allow_redirects=False
    )
    if response.status_code == 200:
        hot_list += response.json().get("data", {}).get("children", [])
        after = response.json().get("data", {}).get("after", "")

        if after:
            return recurse(subreddit, hot_list, after)

        else:
            return hot_list
    else:
        return None
