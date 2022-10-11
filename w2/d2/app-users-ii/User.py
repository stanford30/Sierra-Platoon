class User:
    user_posts = {}

    def __init__(self, name, email, address, drivers_license):
        self.name = name
        self.email = email
        self.address = address
        self.drivers_license = drivers_license
        # initialize user posts
        User.user_posts[self.name] = []

    def post(self, content):
        User.user_posts[self.name] += [content]

    def __str__(self):
        return f'name: {self.name}\nemail: {self.email}\naddress: {self.address}\ndrivers license: {self.drivers_license}'


fifo = User('Fifo', 'fifo99@gmail.com', '123 fake street', '1234123412311')
print(fifo)

fifo.post('hello')
fifo.post('world')
bibo = User('Bibo', 'bibo11@gmail.com', '111 12 street', '111333222111')
bibo.post('first post yay')
print(User.user_posts)