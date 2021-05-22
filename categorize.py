from database import Database
import json
from termcolor import colored
from os import path
import sys

db = Database("sub_db.json")

with open("cats.json", "r") as fl:
    categories = json.load(fl)

args = sys.argv
results = []
processed = []
final_text = ""

for cat in categories:
    print(colored(f"Now generating {cat}", "cyan"))
    final_text += f"<h2>{cat.capitalize()}</h2>\n"
    results = []
    for i in categories[cat]:
        if args[1] == "lev":
            subs_name = db.lev_search_by_key(i)
            subs_desc = db.lev_search_by_value(i)
            for i in subs_name:
                if i[0] not in results:
                    results.append(i[0])
            for i in subs_desc:
                if db.db_inverse[i[0]] not in results:
                    results.append(db.db_inverse[i[0]])
        if args[1] == "regex":
            subs_name = db.regex_search_by_key(i)
            subs_desc = db.regex_search_by_value(i)
            for i in subs_name:
                if i not in results:
                    results.append(i)
            for i in subs_desc:
                if db.db_inverse[i] not in results:
                    results.append(db.db_inverse[i])
    final_text += "\t<ul>\n"
    for result in results:
        final_text += f"\t\t<li><a target='_blank' href='https://www.reddit.com/r/{result}'>r/{result}</a></li>\n"
        processed.append(result)
    final_text += "\t</ul>\n"

final_text += f"<h2>Other</h2>\n"
final_text += "\t<ul>\n"
for i in db.db.keys():
    if i not in processed:
        final_text += f"\t\t<li><a target='_blank' href='https://www.reddit.com/r/{i}'>r/{i}</a></li>\n"
final_text += "\t</ul>\n"


with open("categories.html", "w") as fl:
    fl.write(final_text)

print(
    colored(
        f"Finished generating. Outputted to 'categories.html'", "green", attrs=["bold"]
    )
)
