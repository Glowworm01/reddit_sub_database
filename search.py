from database import Database
from termcolor import colored

db = Database('sub_db.json')

while True:
    query = input("Enter search term: ")
    key_results = db.search_by_key(query)
    value_results = db.search_by_value(query)

    print(colored("By Name: ", 'red', attrs=['bold']))
    for result in key_results:
        name = colored(f"r/{result[0]}:", 'green', attrs=['bold'])
        desc = filter(lambda x: x != '', db.db[result[0]].split("\n"))
        print(name)
        for i in desc:
            print(colored(i, 'blue'))
        print('\n')

    print(colored("By Description: ", 'red', attrs=['bold']))
    for result in value_results:
        name = colored(f"r/{db.db_inverse[result[0]]}:", 'green', attrs=['bold'])
        desc = filter(lambda x: x != '', result[0].split("\n"))
        print(name)
        for i in desc:
            print(colored(i, 'blue'))
        print('\n')