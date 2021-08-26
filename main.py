from enum import Enum, auto


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

        for i in range(7):
            self.game.append(list())

            for j in range(6):
                self.game[i].append(GamePieces.EMPTY)

    def place_piece(self, column: int):
        if self.is_full(column):
            return

        list_of_columns = self.game[column]
        for i in range(6):
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
        for i in range(6):
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





        # diagonals
        pass

    def get_diagonals(self):
        diagonals = list()
        # top left to low right
        for k in range(6 + 7 - 1):
            diagonal = list()
            for j in range(k + 1):
                i = k - j
                if i < 7 and j < 6:
                    diagonal.append(self.game[i][j])
            if len(diagonal) >= 4:
                diagonals.append(diagonal)

        return diagonals





    def is_full(self, column: int):
        for row_element in self.game[column]:
            if row_element == GamePieces.EMPTY:
                return False
        return True

    def get_rows(self, row: int):
        ls = list()
        for column in self.game:
            ls.append(column[row])
        return ls

    def __str__(self):
        output = ""
        list_of_output = list()

        for i in range(6):
            list_of_output.append(self.get_rows(6 - i - 1))

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
    print(board.__str__())


if __name__ == '__main__':
    main()
