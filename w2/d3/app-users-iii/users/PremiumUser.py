# Your PremiumUser class goes here
from User import User


class PremiumUser(User):
    pass


kenny = PremiumUser("kenny", "111@gmail.com", "133 we street", "123021301230")
print(kenny)
