from frame import Frame


class Player:
    def __init__(self, name):
        self.name = name
        self.all_bowls = []
        self.frames = []
        self.all_scores = []

    def bowl(self):
        frame = Frame.generate_frame()
        self.frames.append(frame)
        self.all_bowls.append(frame.tries)

        # print(frame.__dict__)

    def calculate_score(self):
        score = 0
        for i in range(len(self.frames)):
            if self.frames[i].strike:
                try:
                    count = 1
                    while count <= 2:
                        score += sum(self.all_bowls[i + count])
                        if (
                            self.all_bowls[i + count][1] == 0
                            and self.frames[i + count].strike
                        ):
                            count += 1
                        else:
                            count += 2
                except IndexError:
                    pass
            elif self.frames[i].spare:
                try:
                    score += self.all_bowls[i + 1][0]
                except IndexError:
                    pass
            score += sum(self.all_bowls[i])
            self.all_scores.append(score)

        return score


stanley = Player("Stanley")
# stanley.bowl()
# stanley.bowl()
# frame = Frame(10, [10, 0])
# frame2 = Frame(9, [0, 9])
# frame3 = Frame(9, [9, 0])
# frame4 = Frame(10, [9, 1])
# frame5 = Frame(10, [9, 1])
# stanley.frames.append(frame)
# stanley.all_bowls.append(frame.tries)
# stanley.frames.append(frame2)
# stanley.all_bowls.append(frame2.tries)
# stanley.frames.append(frame3)
# stanley.all_bowls.append(frame3.tries)
for i in range(13):
    frame = Frame(10, [10, 0])
    stanley.frames.append(frame)
    stanley.all_bowls.append(frame.tries)
# stanley.frames.append(frame4)
# stanley.all_bowls.append(frame4.tries)
# stanley.frames.append(frame5)
# stanley.all_bowls.append(frame5.tries)
print(len(stanley.frames))
print(stanley.calculate_score())
print(stanley.all_scores[9])
