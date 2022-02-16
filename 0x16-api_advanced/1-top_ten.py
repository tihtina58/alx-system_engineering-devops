#!/usr/bin/python3
"""queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the\
 first 10 hot posts listed for a given subreddit."""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("None")
    else:
        childs = r.json().get("data").get("children")
        first_childs = childs[:10]
        for child in first_childs:
            print(child.get("data").get("title"))
