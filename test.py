from praw import *

reddit = Reddit(
    client_id="p6JgvHLDvRWmAQ",
    client_secret="D5dz1jZ_zPapG0xpup2xeOn5oVINYQ",
    user_agent="windows:reddit.api.stuffs:v1.0.0 (by u/Glowworm04)"
)

sub = reddit.subreddit("randnsfw")

print(sub.display_name)
print(sub.description)