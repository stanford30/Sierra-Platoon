from django.test import TestCase

# Create your tests here.
import json
import os

data_file = "../data/staff.json"

my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, data_file)


with open(file_path) as json_file:
    data = json.load(json_file)
    print(data)
