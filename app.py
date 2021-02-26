from praw import *
from termcolor import colored
import json

reddit = Reddit(
    client_id="p6JgvHLDvRWmAQ",
    client_secret="D5dz1jZ_zPapG0xpup2xeOn5oVINYQ",
    user_agent="windows:reddit.api.stuffs:v1.0.0 (by u/Glowworm04)"
)

subs = {}

def add_to_db(sub):
    name = sub.display_name
    desc = sub.public_description
    subs[name] = desc
    with open("sub_db.json", "w") as fl:
        json.dump(subs, fl, indent=4)

def print_sub(sub):
    name = colored(sub.display_name, 'green', attrs=['bold'])
    desc = colored(sub.public_description, 'blue')
    raw_url = 'https://www.reddit.com' + sub.url
    url = colored(raw_url, 'magenta')
    print('\n' + name + ': ' + url + '\n' + desc)
    
def main():
    while True:
        sub = reddit.subreddit("randnsfw")
        add_to_db(sub)
        print_sub(sub)
        

main()