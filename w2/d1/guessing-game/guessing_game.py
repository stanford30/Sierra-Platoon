class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        self.is_solved = False

    def solved(self):
        return self.is_solved

    def guess(self, num):
        if (num == self.answer):
            self.is_solved = True
            # print('correct')
            return 'correct'
        elif num < self.answer:
            # print('low')
            return 'low'
        else:
            # print('high')
            return 'high'


import random

game = GuessingGame(random.randint(0, 100))
last_guess = None
last_result = None

while game.solved() == False:
    if last_guess != None:
        print(f"Ooops! Your last guess ({last_guess}) was {last_result}.")
        print("")
    last_guess = int(input("Enter your guess: "))
    last_result = game.guess(last_guess)

print(f'{last_guess} was correct!')