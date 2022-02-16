#!/usr/bin/python3
"""requeset number of subscribers for a given subreddit."""
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


def number_of_subscribers(subreddit):
    """requeset number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return 0
    return r.json().get('data').get('subscribers')
