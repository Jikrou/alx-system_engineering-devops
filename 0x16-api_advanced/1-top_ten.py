#!/usr/bin/python3
"""
Function print the titles for the first 10 hot posts for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    user_agent = {'User-agent': 'MyPythonScript/1.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(
            url, headers=user_agent, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])

    else:
        print(None)
