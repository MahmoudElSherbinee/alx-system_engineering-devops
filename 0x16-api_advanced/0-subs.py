#!/usr/bin/python3
"""Get the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    reqest = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"})

    if reqest.status_code == 200:
        return reqest.json().get("data").get("subscribers")
    else:
        return 0
