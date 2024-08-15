#!/usr/bin/python3
"""
function that queries Reddit API and returns
number of subscribers (not active users, total subscribers)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        users = data.get("subscribers")
        return users
    else:
        return 0
