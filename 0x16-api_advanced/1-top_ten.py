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

    if not isinstance(subreddit, str):
        print(None)
        return

    user_agent = {'User-agent': 'MyPythonScript/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        for post in posts[:10]:
            print(post.get('data').get('title'))

    else:
        print(None)
