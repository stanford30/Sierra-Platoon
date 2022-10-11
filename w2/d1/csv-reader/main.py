import csv


# dat = open('./data/dogs.csv', 'r')
# for line in dat:
#     print(line)
class Animal():

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f'{self.name}, is a {self.age} year old {self.breed}'


try:

    animal = input('Which animal would you like to search? ')

    with open('./data/{0}.csv'.format(animal)) as csvfile:
        # for row in csvfile:
        #     print(row)

        csvreader = csv.reader(csvfile, delimiter=",", skipinitialspace=True)
        next(csvreader)

        for name, age, breed in csvreader:
            # print(csvreader.fieldnames())
            # print(name, age, breed)
            dog = Animal(name, age, breed)
            print(dog)
            # dog = Animal(name, age, breed)

except FileNotFoundError:
    print(f'could not find {animal} in the directory')

# print(dat)
