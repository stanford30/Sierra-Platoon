import csv


class Customer:
    def __init__(self, id, account_type, first_name, last_name, current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    # @classmethod
    def all_customers():
        l = []
        with open("data/customers.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customer = Customer(**row)
                l.append(customer)
        return l

    # @classmethod
    # def add_customer(cls, customer):
    #     new_customer = cls(**customer)
    #     self.customers.append(new_customer)


# stanley = Customer(1, "aa", "stanley", "z", "toy story")
# stanley.all_customers()
# joe = Customer(1, "aa", "joe", "S", "toy story")
# print(stanley.customers)
# print(joe.customers)
# my_list = Customer.all_customers()
# my_list.append("hello world")
# print(my_list)
# print(Customer.customers)
# Customer.add_customer({1, "aa", "Joe", "S", "toy story"})
