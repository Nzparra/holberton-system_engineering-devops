#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Reddit Api """
    header = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    rq = requests.get(url, headers=header,
                      params=params, allow_redirects=False)
    if rq.status_code != 200:
        print(None)
        return
    data = rq.json()['data']['children']
    if len(data) == 0:
        print(None)
    else:
        for post in data:
            print(post['data']['title'])
