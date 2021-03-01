from database import Database
from termcolor import colored

db = Database('sub_db.json')

query = input("Enter search term: ")
results = db.search_by_key(query)

for result in results:
    name = colored(f"\tr/{result[0]}:\n", 'green', attrs=['bold'])
    desc = colored(f"\t{db.db[result[0]]}\n", 'blue')
    print(name, desc)