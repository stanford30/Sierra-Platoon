import random


class Frame:
    def __init__(self, score, tries):
        self.score = score
        self.tries = tries
        self.strike = self.strike()
        self.spare = self.spare()

    def strike(self):
        if self.score == 10 and self.tries[1] == 0:
            return True
        return False

    def spare(self):
        if self.score == 10 and self.tries[1] != 0:
            return True
        return False

    @classmethod
    def generate_frame(cls):
        bowl_1 = random.randint(0, 10)
        if bowl_1 != 10:
            bowl_2 = random.randint(0, 10 - bowl_1)
            tries = [bowl_1, bowl_2]
            score = bowl_1 + bowl_2
        else:
            tries = [bowl_1, 0]
            score = bowl_1
        return cls(score, tries)


# frame = Frame(10, [9, 1])
# print(frame.score)
# print(len(frame.tries))
# print(frame.spare)
# print(frame.strike)

# #
