import random


def ai_move(board, moves, playing_as, playing_vs):
    """ Priority in choice of moves:
        Win > Disrupt enemy win > Random move from available moves """
    wins = [board[:5:2], board[6:11:2], board[12::2], board[::6],
            board[2::6], board[4::6], board[::8], board[4:13:4]]
    win_move = ''
    break_move = ''
    for slice in wins:
        if slice.count(playing_as) == 2:
            win_move += ''.join(i for i in slice if i in '123456789')
        if slice.count(playing_vs) == 2:
            break_move += ''.join(i for i in slice if i in '123456789')
    if win_move:
        return win_move[0]
    elif break_move:
        return break_move[0]
    else:
        return random.choice(moves)


