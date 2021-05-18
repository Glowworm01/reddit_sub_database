from database import Database
import json
from termcolor import colored
from os import path

db = Database('sub_db.json')

with open('cats.json', 'r') as fl:
    categories = json.load(fl)

results = []
processed = []
final_text = ''

for cat in categories:
    print(colored(f"Now generating {cat}", 'cyan'))
    final_text += f"<h2>{cat.capitalize()}</h2>\n"
    results = []
    for i in categories[cat]:
        subs_name = db.search_by_key(i)
        subs_desc = db.search_by_value(i)
        for i in subs_name:
            if i[0] not in results:
                results.append(i[0])
        for i in subs_desc:
            if db.db_inverse[i[0]] not in results:
                results.append(db.db_inverse[i[0]])
    final_text += '\t<ul>\n'
    for result in results:
        final_text += f"\t\t<li><a target='_blank' href='https://www.reddit.com/r/{result}'>r/{result}</a></li>\n"
        processed.append(result)
    final_text += '\t</ul>\n'

final_text += f"<h2>Other</h2>\n"
final_text += '\t<ul>\n'
for i in db.db.keys():
    if i not in processed:
        final_text += f"\t\t<li><a target='_blank' href='https://www.reddit.com/r/{i}'>r/{i}</a></li>\n"
final_text += '\t</ul>\n'

print(colored(f"Finished generating. Outputing to 'categories.html'", 'green', attrs=['bold']))
with open('categories.html', 'w') as fl:
    fl.write(final_text)
