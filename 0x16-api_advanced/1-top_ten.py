#!/usr/bin/python3
""" A function that queries the RedditAPI"""
import requests


def top_ten(subreddit):
    """ Script that queries RedditAPI and
        returns the first 10 hot posts listed
        for a given subreddit
    """
    headers = {"User-Agent": "MyBot/1.1"}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()

            posts = data['data']['children']

            for post in posts[0:10]:
                title = post['data']['title']
                print(title)
        except KeyError:
            print(None)
    else:
        print(None)
