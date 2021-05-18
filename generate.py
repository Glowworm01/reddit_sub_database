from praw import *
from termcolor import colored
import json

#super duper secure hide details
with open("client_data.json", "r") as fl: 
    client_data = json.load(fl)

reddit = Reddit(
    client_id=client_data['client_id'],
    client_secret=client_data['client_secret'],
    user_agent=client_data['user_agent']
)

# load the already existing database as to not overwrite it
with open("sub_db.json", "r") as fl: 
    subs = json.load(fl)

# add the sub to the db if it isnt already
def add_to_db(sub): 
    name = sub.display_name
    desc = sub.public_description
    if name not in subs:
        subs[name] = desc
        with open("sub_db.json", "w") as fl:
            json.dump(subs, fl, indent=4)
        print_status(name, success=True)
    else:
        print_status(name, success=False)

# Print whether the sub being added currently is already in the database or not
def print_status(name, success): 
    if success:
        msg = colored(f'Added {name} to database, database now contains {len(subs)} entries.', 'green')
    else:
        msg = colored(f'Databse already contains {name}. Skipping.', 'red')
    print(msg)

# Print the found subreddit in a nice readable format with a clickable link
def print_sub(sub): 
    name = colored(sub.display_name, 'green', attrs=['bold'])
    desc = colored(sub.public_description, 'blue')
    raw_url = 'https://www.reddit.com' + sub.url
    url = colored(raw_url, 'magenta')
    print(f"\n{name}: {url}\n{desc}")

# main loop, finds a subreddit and calls 'add_to_db' with the found subreddit
while True:
    sub = reddit.subreddit("random")
    add_to_db(sub)