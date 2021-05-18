from fuzzywuzzy import process
import json

class Database:
    """The Database class. Can be used to search the database by key or value.
    \nOnly works with a dictionary as the database type."""

    def __init__(self, file):
        # loads the database into a variable 
        # and loads an inverse version where the keys and values are switched
        with open(file) as fl:
            self.db = json.load(fl)
            self.db_inverse = {v: k for k, v in self.db.items()}

    def search_by_key(self, query, limit=200, threshold=80):
        """Searches the database keys by a query."""
        return filter(lambda x: x[1] > threshold, process.extract(query, self.db.keys(), limit=limit))

    def search_by_value(self, query, limit=200, threshold=80):
        """Searches the database values by a query."""
        return filter(lambda x: x[1] > threshold, process.extract(query, self.db.values(), limit=limit))
