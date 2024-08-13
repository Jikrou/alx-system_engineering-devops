#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'MyPythonScript/1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        try:
            return response.json()['data']['subscribers']
        except KeyError:
            return 0
    else:
        return 0
