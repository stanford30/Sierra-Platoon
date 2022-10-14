# # Your User class goes here
class User:
    user_posts = {}

    def __init__(self, name, email, address, drivers_license):
        self.name = name
        self.email = email
        self.address = address
        self.drivers_license = drivers_license
        # initialize user posts
        self.user_posts[self.name] = []

    def post(self, content):
        self.user_posts[self.name] += [content]

    def __str__(self):
        return f"name: {self.name}\nemail: {self.email}\naddress: {self.address}\ndrivers license: {self.drivers_license}"


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     @classmethod
#     def margherita(cls):
#         return cls(["mozzarella", "tomatoes"])

#     @classmethod
#     def prosciutto(cls):
#         return cls(["mozzarella", "tomatoes", "ham"])


# p = Pizza.prosciutto()
# print(p.ingredients)
