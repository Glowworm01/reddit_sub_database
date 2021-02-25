from praw import *
from termcolor import colored
import json
from time import sleep

reddit = Reddit(
    client_id="p6JgvHLDvRWmAQ",
    client_secret="D5dz1jZ_zPapG0xpup2xeOn5oVINYQ",
    user_agent="windows:reddit.api.stuffs:v1.0.0 (by u/Glowworm04)"
)

history = []

def print_sub(sub):
    name = colored(sub.display_name, 'green', attrs=['bold'])
    desc = colored(sub.public_description, 'blue')
    raw_url = 'https://www.reddit.com' + sub.url
    url = colored(raw_url, 'magenta')
    print('\n' + name + ': ' + url + '\n' + desc)
    
def save_to_file(sub):
    pass

def check_history(sub):
    if sub.display_name in history:
        return False
    else:
        history.append(sub.display_name)
        return True

def main():
    while True:
        sub = reddit.subreddit("randnsfw")
        if check_history(sub):
            print_sub(sub)
            save_to_file(sub)
        sleep(1)
        

main()