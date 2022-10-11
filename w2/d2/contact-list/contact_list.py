class ContactList:
    # contact_lists = []

    def __init__(self, list_name, contact_list):
        self.list_name = list_name
        # contact_list.sort(key=lambda x: x['name'])
        self.contact_list = sorted(contact_list, key=lambda x: x['name'])
        # self.contact_list = contact_list
        # ContactList.contact_lists.extend([self.list_name, self.contact_list])

    def add_contact(self, contact):
        self.contact_list.append(contact)
        self.contact_list = sorted(self.contact_list, key=lambda x: x['name'])


friends = [{
    'name': 'Bob',
    'number': '555-5555'
}, {
    'name': 'Alice',
    'number': '867-5309'
}]
work_buddies = [{
    'name': 'Alice',
    'number': '867-5309'
}, {
    'name': 'Carlos',
    'number': '555-5555'
}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
my_friends_list.add_contact({'name': 'Billy', 'number': '123-1111'})
my_friends_list.add_contact({'name': 'Alan', 'number': '123-1112'})
print(my_friends_list.contact_list)