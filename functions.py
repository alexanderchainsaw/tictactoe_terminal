from colorama import Fore, Style

yellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL

x = f'{red}X{reset}'
o = f'{green}O{reset}'


def won(board):
    """ Determine whether the current board contains a win
        by converting winning board slices into a set
        If returned value is 2, then 2 win conditions reached == double win"""
    wins = [board[:5:2], board[6:11:2], board[12::2], board[::6],
            board[2::6], board[4::6], board[::8], board[4:13:4]]
    return sum(1 for item in wins if len(set(item)) == 1)


def board_display(board, draw=False):
    """ Paint X and O elements with their colors by replacing string X's and O's
        with painted objects, if there is a draw - paint it yellow """
    if not draw:
        print(f'{"-" * 37}\n'
              f'{" " * 15}{board.replace("X", x).replace("O", o).split()[0]}\n'
              f'{" " * 15}{board.replace("X", x).replace("O", o).split()[1]}\n'
              f'{" " * 15}{board.replace("X", x).replace("O", o).split()[2]}\n'
              f'{"-" * 37}')
    else:
        print(f'{"-" * 37}\n'
              f'{" " * 15}{board.replace("X",f"{yellow}X{reset}").replace("O", f"{yellow}O{reset}").split()[0]}\n'
              f'{" " * 15}{board.replace("X",f"{yellow}X{reset}").replace("O", f"{yellow}O{reset}").split()[1]}\n'
              f'{" " * 15}{board.replace("X",f"{yellow}X{reset}").replace("O", f"{yellow}O{reset}").split()[2]}\n'
              f'{"-" * 37}')


def score_display(x_wins, o_wins):
    """ Display overall score """
    print(f'{" " * 15}Score:\n'
          f'{" " * 15}{x}: {x_wins}\n'
          f'{" " * 15}{o}: {o_wins}\n'
          f'{"-" * 37}')


def first_move(flag: bool):
    if flag:
        print(f'{"-" * 37}\n'
              f'{red}{"First move belongs to X!" : ^37}{reset}\n'
              f'{"-" * 37}')
    else:
        print(f'{"-" * 37}\n'
              f'{green}{"First move belongs to O!" : ^37}{reset}\n'
              f'{"-" * 37}')


def game_over(winner):
    if winner == 'x':
        print(f'{"-"*37}\n'
              f'{red}{"X Victory!" : ^37}{reset}\n'
              f'{"-"*37}')
    elif winner == 'o':
        print(f'{"-"*37}\n'
              f'{green}{"O Victory!" : ^37}{reset}\n'
              f'{"-"*37}')
    else:
        print(f'{"-" * 37}\n'
              f'{yellow}{"Draw!" : ^37}{reset}\n'
              f'{"-" * 37}')
