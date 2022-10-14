# Import and create your users here
from users.FreeUser import FreeUser

stanford = FreeUser("stanford", "stanford@email", "111", "111")
stanford.post(1)
stanford.post(2)
stanford.post(3)
stanford.post(4)
print(stanford.user_posts)
