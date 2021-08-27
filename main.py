from enum import Enum, auto
from globals import *


class GamePieces(Enum):
    RED = "R"
    WHITE = "W"
    EMPTY = "X"


class Player(Enum):
    RED = auto()
    WHITE = auto()

    def get_other_player(self):

        if self.value == Player.RED:
            return Player.WHITE
        return Player.RED

    def get_game_piece(self):
        if self.value == Player.RED:
            return GamePieces.RED
        return GamePieces.WHITE


class GameBoard:

    def __init__(self):
        self.currentPlayer = Player.RED
        self.game = []

        for i in range(WIDTH):
            self.game.append(list())

            for _ in range(HEIGHT):
                self.game[i].append(GamePieces.EMPTY)

    def place_piece(self, column: int):
        if self.is_full(column):
            return

        list_of_columns = self.game[column]
        for i in range(HEIGHT):
            row_element = list_of_columns[i]

            if row_element == GamePieces.EMPTY:
                if self.currentPlayer == Player.RED:
                    self.game[column][i] = GamePieces.RED
                    self.currentPlayer = Player.WHITE
                else:
                    self.game[column][i] = GamePieces.WHITE
                    self.currentPlayer = Player.RED

                return

    def check_win(self):
        # rows
        for i in range(HEIGHT):
            current = self.currentPlayer
            counter = 0
            for row in self.get_rows(i):
                if row == GamePieces.EMPTY or current.get_other_player().get_game_piece():
                    counter = 0

                if row == current.get_game_piece():
                    counter += 1

                if counter == 4:
                    return True

        # columns

        for column in self.game:
            current = self.currentPlayer
            counter = 0
            for row in column:
                if row == GamePieces.EMPTY or current.get_other_player().get_game_piece():
                    counter = 0
                    continue
                if row == current.get_game_piece():
                    counter += 1

                if counter == 4:
                    return True

        for diagonals in self.get_diagonal_one() + self.get_diagonal_two():
            current = self.currentPlayer
            counter = 0
            for diagonal in diagonals:
                if diagonal == GamePieces.EMPTY or current.get_other_player().get_game_piece():
                    counter = 0
                    continue
                if diagonal == current.get_game_piece():
                    counter += 1

                if counter == 4:
                    return True

        return False

    def get_diagonal_one(self):
        diagonals = list()
        # top left to low right
        for k in range(HEIGHT + WIDTH - 1):
            diagonal = []
            for j in range(k + 1):
                i = k - j
                if i < WIDTH and j < HEIGHT:
                    diagonal.append(self.game[i][j])
            if len(diagonal) >= 4:
                diagonals.append(diagonal)

        return diagonals

    def get_diagonal_two(self):
        diagonals = []
        for d in range(HEIGHT + WIDTH - 1):
            diagonal = []
            i = 0
            j = 0
            while i >= HEIGHT or j >= WIDTH:
                i = HEIGHT - d - 1 if d < HEIGHT else 0
                j = 0
                if d >= HEIGHT:
                    j = d - HEIGHT + 1
                diagonal.append(self.game[i][j])
                if i >= HEIGHT or j >= WIDTH:
                    break
                i += 1
                j += 1

            if len(diagonal) >= 4:
                diagonals.append(diagonal)
        return diagonals

    def is_full(self, column: int):
        return GamePieces.EMPTY not in self.game[column]

    def get_rows(self, row: int):
        return [column[row] for column in self.game]

    def __str__(self):
        output = ""
        list_of_output = [self.get_rows(6 - i - 1) for i in range(6)]

        for row in list_of_output:
            for element in row:
                output += element.value + ","
            output += "\n"
        return output


def main():
    board = GameBoard()
    print(board.__str__())
    board.place_piece(1)
    board.place_piece(1)
    board.place_piece(1)
    board.place_piece(1)
    board.place_piece(1)
    board.place_piece(1)
    board.place_piece(2)
    board.place_piece(2)
    board.place_piece(2)
    board.place_piece(2)

    print(board.__str__())

    board.get_diagonal_one()


if __name__ == '__main__':
    main()
