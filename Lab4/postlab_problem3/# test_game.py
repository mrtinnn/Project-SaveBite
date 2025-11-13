# test_game.py

import unittest
from oxo_logic_game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_board_empty(self):
        self.assertEqual(self.game.board, [' '] * 9)

    def test_make_move_valid(self):
        self.assertTrue(self.game.make_move(0))
        self.assertEqual(self.game.board[0], 'X')

    def test_make_move_invalid(self):
        self.game.make_move(0)
        self.assertFalse(self.game.make_move(0))  # cannot move on occupied
        self.assertFalse(self.game.make_move(-1)) # out of bounds
        self.assertFalse(self.game.make_move(9))  # out of bounds

    def test_toggle_player(self):
        self.assertEqual(self.game.current_player, 'X')
        self.game.make_move(0)
        self.assertEqual(self.game.current_player, 'O')
        self.game.make_move(1)
        self.assertEqual(self.game.current_player, 'X')

    def test_check_winner_row(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'X')

    def test_check_winner_column(self):
        self.game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertEqual(self.game.check_winner(), 'O')

    def test_check_winner_diagonal(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertEqual(self.game.check_winner(), 'X')

    def test_no_winner_yet(self):
        self.assertIsNone(self.game.check_winner())

    def test_is_full(self):
        self.game.board = ['X','O','X','O','X','O','X','O','X']
        self.assertTrue(self.game.is_full())
        self.game.board[0] = ' '
        self.assertFalse(self.game.is_full())

if __name__ == "__main__":
    unittest.main()
