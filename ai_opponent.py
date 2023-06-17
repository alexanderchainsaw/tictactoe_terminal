import random


def ai_move(board, moves, playing_as, playing_vs):
    """ Priority in choice of moves:
        Win -> Disrupt enemy win ->
        -> Random secondary move (cell 5 is the priority) ->
        -> Random move from available (cell 5 is the priority)"""
    wins = [board[:5:2], board[6:11:2], board[12::2], board[::6],
            board[2::6], board[4::6], board[::8], board[4:13:4]]
    win_moves = ''
    break_moves = ''
    secondary_move = ''.join(''.join(i for i in x if i in '123456789')
                             for x in wins if playing_as in x and playing_vs not in x)
    for x in wins:
        if x.count(playing_as) == 2:
            win_moves += ''.join(i for i in x if i in '123456789')
        if x.count(playing_vs) == 2:
            break_moves += ''.join(i for i in x if i in '123456789')
    if win_moves:
        return win_moves[0]
    elif break_moves:
        return break_moves[0]
    elif secondary_move:
        return '5' if '5' in secondary_move else random.choice(secondary_move)
    else:
        return '5' if '5' in moves else random.choice(moves)


