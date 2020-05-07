#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Reddit Api """
    header = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    rq = requests.get(url, headers=header, allow_redirects=False)
    if rq.status_code != 200:
        return 0
    data = rq.json()
    if 'data' not in data:
        return 0
    if 'subscribers' not in data.get('data'):
        return 0
    return rq.json()['data']['subscribers']
