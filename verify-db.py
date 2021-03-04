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

def check_sub(sub):
    subreddit = reddit.subreddit(sub)
    try:
        verify = subreddit.description
        clean_db[subreddit.display_name] = subreddit.public_description
        print(colored(f"The subreddit '{sub}' is valid.", 'green'))
    except:
        print(colored(f"The subreddit '{sub}' is invalid. Removing it from database.", 'red'))

print(colored("This may take some time", 'cyan', attrs=['bold']))
for sub in db:
    check_sub(sub)

with open("sub_db.json", "w") as fl:
    json.dump(clean_db, fl, indent=4)