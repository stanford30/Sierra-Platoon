from User import User


class FreeUser(User):
    # def __init__(self, name, email, address, drivers_license):
    #     super().__init__(name, email, address, drivers_license)

    def post(self, content):
        # print(self.user_posts[self.name].__len__())
        if self.user_posts[self.name].__len__() > 1:
            print("Free Users can only make two posts, sorry")
            return "Free Users can only post twice."
        super().post(content)


stanford = FreeUser("stanford", "stanford@email", "111", "111")
stanford.post(1)
stanford.post(2)
stanford.post(3)
stanford.post(4)
print(stanford.user_posts)
