#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if request.status_code == 200:
        for get_data in request.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            print(title)
    else:
        print(None)
