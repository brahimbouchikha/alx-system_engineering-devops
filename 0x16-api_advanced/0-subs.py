#!/usr/bin/python3
"""
function that queries Reddit API and returns
number of subscribers (not active users, total subscribers)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = f"https://www.reddit.com/r/{}/about.json"
    headers = {"User-Agent": "brahimbouchikha"}
    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
