from database import Database
import json
from termcolor import colored

db = Database('sub_db.json')

with open('cats.json', 'r') as fl:
    categories = json.load(fl)

results = []
final_text = ''

for cat in categories:
    print(colored(f"Now generating {cat}", 'cyan'))
    final_text += f"\n---{cat.capitalize()}---\n"
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
    for result in results:
        final_text += f"{result}\n"
print(colored(f"Finished generating. Outputing to 'categories.txt'", 'green', attrs=['bold']))
with open('categories.txt', 'w') as fl:
    fl.write(final_text)
