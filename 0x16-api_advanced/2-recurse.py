#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def add(hot_list, data):
    "" "Add data in a list """
    if len(data) == 0:
        return
    hot_list.append(data[0]['data']['title'])
    data.pop(0)
    add(hot_list, data)


def recurse(subreddit, hot_list=[], after=None):
    """ Reddit Api """
    header = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after,
              'limit': 100}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    rq = requests.get(url, headers=header,
                      params=params, allow_redirects=False)
    if rq.status_code != 200:
        return None
    dic = rq.json()
    data = dic['data']['children']
    add(hot_list, data)
    dic2 = dic['data']['after']
    if not dic2:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=dic2)
