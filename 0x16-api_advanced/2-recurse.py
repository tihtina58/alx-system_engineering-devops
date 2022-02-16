#!/usr/bin/python3
"""returns a list containing the titles of
 all hot articles for a given subreddit."""
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles of
all hot articles for a given subreddit."""
    if len(hot_list) != 0:
        page = hot_list[0]
    else:
        page = ''
        hot_list.append('')

    url = 'https://www.reddit.com/r/' + subreddit
    url += '/hot.json?limit=100&after=' + page
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return None
    else:
        data = r.json().get("data")
        after = data.get("after")
        hot_list[0] = after

        childs = data.get("children")
        for child in childs:
            hot_list.append(child.get("data").get("title"))
        if after is None:
            return hot_list[1:]
        return recurse(subreddit, hot_list)
