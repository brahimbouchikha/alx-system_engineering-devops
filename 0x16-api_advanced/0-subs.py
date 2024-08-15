#!/usr/bin/python3
"""
function that queries Reddit API and returns
number of subscribers (not active users, total subscribers)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    """

    respoonse = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False
    )
    if respoonse.status_code == 404:
        return 0
    else:
        data = respoonse.json()
        return data.get('data').get('subscribers')
