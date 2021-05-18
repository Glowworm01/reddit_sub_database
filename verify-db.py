from praw import *
from termcolor import colored
import json

with open("client_data.json", "r") as fl:
    client_data = json.load(fl)

reddit = Reddit(
    client_id=client_data['client_id'],
    client_secret=client_data['client_secret'],
    user_agent=client_data['user_agent']
)

with open("sub_db.json", "r") as fl:
    db = json.load(fl)

clean_db = {}
processed = 0

def check_sub(sub):
    subreddit = reddit.subreddit(sub)
    try:
        verify = subreddit.description
        clean_db[subreddit.display_name] = subreddit.public_description
        print(colored(f"The subreddit '{sub}' is valid. ({len(db)-processed} left)", 'green'), )
        
    except:
        print(colored(f"The subreddit '{sub}' is invalid. Removing it from database. ({len(db)-processed} left)", 'red'))
        
print(colored("This may take some time", 'cyan', attrs=['bold']))
for sub in db:
    processed += 1
    check_sub(sub)

with open("sub_db.json", "w") as fl:
    json.dump(clean_db, fl, indent=4)