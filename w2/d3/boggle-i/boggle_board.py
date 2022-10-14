import string
import random


class BoggleBoard:
    board_rows = 4
    game_board = ["_" * 4 for x in range(board_rows)]
    # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = string.ascii_uppercase

    def __init__(self):
        self.init_board()

    def shake(self):

        new_board = [self.generate_row(4) for row in self.game_board]
        # for row in self.game_board:
        #     str1 = ""
        #     for letter in row:

        #         letter = self.alphabet[random.randint(0, 25)]
        #         str1 += letter
        #     new_board.append(str1)
        # print(new_board)
        self.game_board = new_board
        print("\n".join(self.game_board))

    def init_board(self):
        print("\n".join(self.game_board))

    def generate_row(self, num):
        def generate_letter(num):
            string1 = ""
            for x in range(num):
                string1 += f"{self.alphabet[random.randint(0,25)]}"
            return string1

        return generate_letter(num)


boggle = BoggleBoard()
boggle.shake()
