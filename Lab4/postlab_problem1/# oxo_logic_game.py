# oxo_logic_game.py

class Game:
    def __init__(self):
        self.board = [' '] * 9  # 3x3 board
        self.current_player = 'X'

    def display_board(self):
        b = self.board
        print(f"{b[0]} | {b[1]} | {b[2]}")
        print("--+---+--")
        print(f"{b[3]} | {b[4]} | {b[5]}")
        print("--+---+--")
        print(f"{b[6]} | {b[7]} | {b[8]}")

    def make_move(self, position):
        """Place the current player's mark at position (0-8)."""
        if position < 0 or position > 8:
            return False
        if self.board[position] != ' ':
            return False
        self.board[position] = self.current_player
        self.toggle_player()
        return True

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        """Return 'X', 'O' if someone won, or None."""
        b = self.board
        lines = [
            [0,1,2],[3,4,5],[6,7,8],  # rows
            [0,3,6],[1,4,7],[2,5,8],  # columns
            [0,4,8],[2,4,6]           # diagonals
        ]
        for line in lines:
            if b[line[0]] == b[line[1]] == b[line[2]] != ' ':
                return b[line[0]]
        return None

    def is_full(self):
        return ' ' not in self.board


if __name__ == "__main__":
    game = Game()
    game.display_board()
