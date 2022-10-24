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
                return f"{customer.first_name}'s currently renting videos: {' '.join(customer.current_video_rentals.split('/'))}"

    def get_inventory(self):
        res = []
        for item in self.inventory:
            i = {}
            i["id"] = item.id
            i["title"] = item.title
            i["copies_available"] = item.copies_available
            i["rating"] = item.rating
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
        customer["current_video_rentals"] = ""
        new_customer = Customer(**customer)
        self.customers.append(new_customer)

    def rent_video(self, title, customer_id):
        try:
            customer_found = self.customers[customer_id - 1]
        except IndexError:
            print("No customer found with that ID")
            return "No customer found with that ID"

        current_videos = self.get_customer_rented_videos_by_id(customer_id)
        current_videos = current_videos.split("\n")

        if title in current_videos:
            print(f"Customer is already renting {title}")
            return

        account_type = customer_found.account_type
        # customer_id = customer_found.id

        # sx = standard account: max 1 rental at a time
        # px = premium account: max 3 rentals out at a time
        # "sf" = standard family account: max 1 rental at a time AND can not rent any "R" rated movies
        # "pf" = premium family account: max 3 rentals at a time and can not rent any "R" rated movies

        family_account, standard_account, max_videos = self.find_account_info(
            account_type
        )

        video_id, video_found = self.find_video(title)

        if video_found["rating"] == "R" and family_account:
            return 'Can not rent "R" Rated movies on family account'
        if len(current_videos) >= max_videos:
            print("Max number of videos account can rent has exceeded")
            return "Max number of videos account can rent has exceeded"
        if video_found["copies_available"] == "0":
            print(f"Currently 0 copies of {title} available")
            return f"Currently 0 copies of {title} available"

        self.customers[int(customer_id) - 1].current_video_rentals += f"/{title}"
        # print(self.customers[int(customer_id) - 1].current_video_rentals)
        copies_available = int(self.inventory[int(video_id) - 1].copies_available)
        self.inventory[int(video_id) - 1].copies_available = str(copies_available - 1)
        res = []
        res.append(
            f"successfully rented out {title} into {customer_found.first_name}'s account"
        )
        res.append(self.get_customer_rented_videos_by_id(customer_id))
        print("\n".join(res))
        # print(self.inventory[int(video_id) - 1].copies_available)
        # print(account_type[1])
        # print(current_videos)

        # print(type(current_videos))

    def find_account_info(self, account_type):
        family_account = False
        if account_type[1] == "f":
            family_account = True

        standard_account = False
        if account_type[0] == "s":
            standard_account = True

        if standard_account:
            max_videos = 1
        else:
            max_videos = 3
        return family_account, standard_account, max_videos

    def find_video(self, title):
        inventory = self.get_inventory()
        video_found = None
        for video in inventory:
            if video["title"] == title:
                video_found = video

        if video_found == None:
            print("Can not find that movie title")
            return "Can not find that movie title"

        video_id = video_found["id"]
        return video_id, video_found

    def return_video(self, customer_id, title):
        try:
            customer_found = self.customers[customer_id - 1]
        except IndexError:
            print("No customer found with that ID")
            return "No customer found with that ID"


store = Store()
# print(store.title_and_copies)
# print(store.customers)
# store.add_customer(
#     {
#         "id": 5,
#         "account_type": "aa",
#         "first_name": "stanley",
#         "last_name": "z",
#         "current_video_rentals": "toy story",
#     }
# )
# store.add_customer({7, "aa", "stanley", "z", "toy story"})
# print(store.customers)
# print(store.get_customer_rented_videos_by_id(6))
store.rent_video("Intersteller", 6)

# print(store.get_customers())
