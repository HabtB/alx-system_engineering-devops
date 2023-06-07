#!/usr/bin/python3
""" A recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ A recursive function that queries the Reddit API
    and returns a list contraining the titles of all hot
    articles for a given subreddit.
    """
    headers = {'User-Agent': 'MyScript/1.0'}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            if 'after' in data['data']:
                after = data['data']['after']
                return recurse(subreddit, hot_list=hot_list, after=after)

        except KeyError:
            return None
        return hot_list
    else:
        return None
