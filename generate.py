from praw import *
from termcolor import colored
import json

reddit = Reddit(
    client_id="p6JgvHLDvRWmAQ",
    client_secret="D5dz1jZ_zPapG0xpup2xeOn5oVINYQ",
    user_agent="windows:reddit.api.stuffs:v1.0.0 (by u/Glowworm04)"
)

with open("sub_db.json", "r") as fl:
    subs = json.load(fl)

def add_to_db(sub): # add the sub to the db if it isnt already
    name = sub.display_name
    desc = sub.public_description
    if name not in subs:
        subs[name] = desc
        with open("sub_db.json", "w") as fl:
            json.dump(subs, fl, indent=4)
        print_status(name, success=True)
    else:
        print_status(name, success=False)

def print_status(name, success): # Print whether the current sub is already in the database or not
    if success:
        msg = colored(f'Added {name} to database, database now contains {len(subs)} entries.', 'green')
    else:
        msg = colored(f'Databse already contains {name}. Skipping.', 'red')
    print(msg)

def print_sub(sub): # Print the found subreddit in a nice readable format
    name = colored(sub.display_name, 'green', attrs=['bold'])
    desc = colored(sub.public_description, 'blue')
    raw_url = 'https://www.reddit.com' + sub.url
    url = colored(raw_url, 'magenta')
    print(f"\n{name}: {url}\n{desc}")

while True:
    sub = reddit.subreddit("random")
    add_to_db(sub)
