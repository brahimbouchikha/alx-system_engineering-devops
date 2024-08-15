#!/usr/bin/python3
"""
function that queries Reddit API and returns
number of subscribers (not active users, total subscribers)
"""

import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return "OK"
    else:
        return 0
