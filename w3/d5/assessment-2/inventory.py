import csv
import os.path


class Inventory:
    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    @classmethod
    def get_inventory(cls):
        inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./data/inventory.csv")

        with open(path) as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
            inventory.append(cls(**row))
        
        return inventory
