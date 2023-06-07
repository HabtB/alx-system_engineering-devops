#!/usr/bin/python3
""" A script that queries RedditAPI and returns the
    number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ A function queries the RedditAPI
        to return the number of subscribers
    """
    headers = {'User-Agent': "MyBot/1.0"}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            return 0
    else:
        return 0
