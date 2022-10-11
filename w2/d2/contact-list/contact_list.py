class ContactList:
    # contact_lists = []

    def __init__(self, list_name, contact_list):
        self.list_name = list_name
        # contact_list.sort(key=lambda x: x['name'])
        self.contact_list = sorted(contact_list, key=lambda x: x["name"])
        # self.contact_list = contact_list
        # ContactList.contact_lists.extend([self.list_name, self.contact_list])

    def add_contact(self, contact):
        self.contact_list.append(contact)
        self.contact_list = sorted(self.contact_list, key=lambda x: x["name"])

    def remove_contact(self, contact_name):
        self.contact_list = list(
            filter(lambda x: x["name"] != contact_name, self.contact_list)
        )

    def find_shared_contacts(self, contact_list):

        return list(filter(lambda x: x in contact_list.contact_list, self.contact_list))


friends = [
    {"name": "Bob", "number": "555-5555"},
    {"name": "Alice", "number": "867-5309"},
]
work_buddies = [
    {"name": "Alice", "number": "867-5309"},
    {"name": "Carlos", "number": "555-5555"},
]

my_friends_list = ContactList("My Friends", friends)
my_work_buddies = ContactList("Work Buddies", work_buddies)
my_friends_list.add_contact({"name": "Billy", "number": "123-1111"})
my_friends_list.add_contact({"name": "Alan", "number": "123-1112"})
my_friends_list.add_contact({"name": "Carlos", "number": "555-5555"})
my_work_buddies.add_contact({"name": "Alan", "number": "123-1112"})
my_friends_list.remove_contact("Billy")

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)
# print(my_friends_list.contact_list)
