# Redit sub database
This utility allows you to generate a database of random subreddits and then search through them or categorize them.

## How to use
The tool rquires a few dependencies before beginning:
- termcolor
- praw
- fuzzywuzzy


### Accessing the Reddit API
In order for the tool to work you must create a Reddit app, you can do that at [here](https://old.reddit.com/prefs/apps/).
Once you have created the app, create a json file called `client_data.json` and fill it with the information below.
```json
{
    "client_id": "<your id>",
    "client_secret": "<your secret>",
    "user_agent": "<your user agent>"
}
```

### Generating the database
Now that the tool can access the Reddit API, you can run `generate.py`. This will create a file called `sub_db.json` containing key value pairs of the subreddit name and description.
It will likely take many hours to generate a databse containing anything more than the top subreddits due to the way the Reddit API works.

### Categorising
The tool can attribute keywords to subreddits by searching through the names and descriptions and then output a list of categorised subreddits in a nice HTML format. This can be done by running `categorize.py` with either the `regex` argument or the `lev` argument, the latter uses the [Levenshtein-Distance Formula](https://en.wikipedia.org/wiki/Levenshtein_distance) and is quite slow, and inaccurate compared to the Regular Expressions method; the RegEx method is much faster but requires the categories to be very specific. No matter what method you choose it does require a little assembly.
In order for the tool to be able to determine what keywords fit into what categories the user must specify. This can be done by creating a file called `cats.json`.
The `cats.json` is easier to show then explain.
```json
{
    "Gaming": [
        "gaming",
        "pc",
        "gamer"
    ],
    "Tech": [
        "computer",
        "programming",
        "tech"
    ],
    "Cars": [
        "cars",
        "racing",
        "f1",
        "engine"
    ],
}
```
As you can see, the format is a category title followed by the keywords it should contain. The category almost always will contain the title as a keywords as the program does not include titles into its search. When using the RegEx method the keywords are case-sensitive so you may be better off with something like this:
```json
{
    "Cars": [
        "cars",
        "Cars",
        "racing",
        "Racing",
        "f1",
        "F1",
        "engine",
        "Engine"
    ]
}
```
 Any subreddits not found during the categorisation are listed under the "Uncategorised" category.

### Searching
When running the `search.py` script the usage is pretty self-explanatory. Enter a search term and the program will return a list of matching subreddit titles and matching subreddit descriptions. Note this method will only user the levenshtein method.

## TODO
- ~~Improve search functionality~~
- Improve database generation
