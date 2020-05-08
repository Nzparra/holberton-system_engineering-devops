#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests
import re


def add(hot_list, data):
    "" "Add data in a list """
    if len(data) == 0:
        return
    title = data[0]['data']['title'].split()
    for idx in title:
        for i in hot_list.keys():
            d = re.compile("^{}$".format(i), re.I)
            if d.findall(idx):
                hot_list[i] += 1
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


def count_words(subreddit, word_list):
    """ Count function """
    dic = {}
    for word in word_list:
        dic[word] = 0
    recurse(subreddit, dic)
    lst = sorted(dic.items(), key=lambda kv: kv[1])
    lst.reverse()
    if len(lst) != 0:
        for idx in lst:
            if idx[1] != 0:
                print("{}: {}".format(idx[0], idx[1]))
    else:
        print()
