from customers import Customer
from inventory import Inventory


class Store:
    def __init__(self):
        # self.name = name
        self.customers = Customer.all_customers()
        self.inventory = Inventory.get_inventory()
        self.id_and_name = self.get_customers()
        self.title_and_copies = self.get_inventory()

    def get_customer_rented_videos_by_id(self, id):
        # print(id)
        for customer in self.customers:
            if int(customer.id) == id:
                return "\n".join(customer.current_video_rentals.split("/"))

    def get_inventory(self):
        res = []
        for item in self.inventory:
            i = {}
            i["title"] = item.title
            i["copies_available"] = item.copies_available
            res.append(i)
        return res

    def get_customers(self):
        res = []
        for c in self.customers:
            d = {}
            d["id"] = c.id
            # name = c.first_name + " " + c.last_name
            d["first_name"] = c.first_name
            d["last_name"] = c.last_name
            res.append(d)
        return res

    def add_customer(self, customer):
        customer["id"] = len(self.customers) + 1
        new_customer = Customer(**customer)
        self.customers.append(new_customer)


store = Store()
# print(store.title_and_copies)
# print(store.customers)
print(store.get_customer_rented_videos_by_id(2))
store.add_customer(
    {
        "id": 5,
        "account_type": "aa",
        "first_name": "stanley",
        "last_name": "z",
        "current_video_rentals": "toy story",
    }
)
# store.add_customer({7, "aa", "stanley", "z", "toy story"})
# print(store.customers)
print(store.get_customers())
