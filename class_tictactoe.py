import random
from class_paint import x, o, Paint


class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.moves = '123456789'
        self.score_x, self.score_o = 0, 0

    def __str__(self):
        return str(self.board)

    def move(self, move, player):
        if move in self.moves:
            self.board = self.board.replace(move, player)
            self.moves = self.moves.replace(move, '')
            return True
        return False

    def won(self):
        """ Determine whether the current board contains a win
            by converting winning board slices into a set
            If returned value is 2, then 2 win conditions reached == double win"""
        board = self.board
        wins = [board[:5:2], board[6:11:2], board[12::2], board[::6],
                board[2::6], board[4::6], board[::8], board[4:13:4]]
        return sum(1 for slce in wins if len(set(slce)) == 1)

    def display_board(self, draw=False):
        brd = self.board
        if not draw:
            return (f'{"-" * 37}\n'
                    f'{" " * 15}{brd.replace("X", x.red()).replace("O", o.green()).split()[0]}\n'
                    f'{" " * 15}{brd.replace("X", x.red()).replace("O", o.green()).split()[1]}\n'
                    f'{" " * 15}{brd.replace("X", x.red()).replace("O", o.green()).split()[2]}\n'
                    f'{"-" * 37}')
        else:
            return (f'{"-" * 37}\n'
                    f'{" " * 15}{brd.replace("X", x.yellow()).replace("O", o.yellow()).split()[0]}\n'
                    f'{" " * 15}{brd.replace("X", x.yellow()).replace("O", o.yellow()).split()[1]}\n'
                    f'{" " * 15}{brd.replace("X", x.yellow()).replace("O", o.yellow()).split()[2]}\n'
                    f'{"-" * 37}')

    def score_display(self):
        """ Display overall score """
        print(f'{" " * 15}Score:\n'
              f'{" " * 15}{x.red()}: {self.score_x}\n'
              f'{" " * 15}{o.green()}: {self.score_o}\n'
              f'{"-" * 37}')

    def ai_move(self, playing_as, playing_vs):
        """ Priority in choice of moves:
            Win -> Disrupt enemy win ->
            -> Random secondary move (cell 5 is the priority) ->
            -> Random move from available (cell 5 is the priority)"""
        board = self.board
        wins = [board[:5:2], board[6:11:2], board[12::2], board[::6],
                board[2::6], board[4::6], board[::8], board[4:13:4]]
        win_moves, break_moves = '', ''
        secondary_move = ''.join(''.join(i for i in j if i in '123456789')
                                 for j in wins if playing_as in j and playing_vs not in j)
        for slce in wins:
            if slce.count(playing_as) == 2:
                win_moves += ''.join(i for i in x if i in '123456789')
            if slce.count(playing_vs) == 2:
                break_moves += ''.join(i for i in x if i in '123456789')
        if win_moves:
            return win_moves[0]
        elif break_moves:
            return break_moves[0]
        elif secondary_move:
            return '5' if '5' in secondary_move else random.choice(secondary_move)
        else:
            return '5' if '5' in self.moves else random.choice(self.moves)


testing = TicTacToe('1-2-3\n4-5-6\n7-8-9')
print(Paint(testing.moves).red())
testing.move('1', 'X')
print(testing)
print(testing.display_board(draw=True))
