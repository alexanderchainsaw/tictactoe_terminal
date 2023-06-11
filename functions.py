from colorama import Fore, Style

x = f'{Fore.RED}X{Style.RESET_ALL}'
o = f'{Fore.GREEN}O{Style.RESET_ALL}'

def won(board):
    wins = [board[:5:2], board[6:11:2], board[12::2], board[::6], board[2::6], board[4::6], board[::8], board[4:13:4]]
    if any(True for x in wins if len(set(x)) == 1):
        return True

def board_display(board, draw=False):
    if not draw:
        print(f'{"-" * 37}\n'
              f'{" " * 15}{board.replace("X", x).replace("O", o).split()[0]}\n'
              f'{" " * 15}{board.replace("X", x).replace("O", o).split()[1]}\n'
              f'{" " * 15}{board.replace("X", x).replace("O", o).split()[2]}\n'
              f'{"-" * 37}')
    else:
        print(f'{"-" * 37}\n'
              f'{" " * 15}{board.replace("X",f"{Fore.LIGHTYELLOW_EX}X{Style.RESET_ALL}").replace("O", f"{Fore.LIGHTYELLOW_EX}O{Style.RESET_ALL}").split()[0]}\n'
              f'{" " * 15}{board.replace("X",f"{Fore.LIGHTYELLOW_EX}X{Style.RESET_ALL}").replace("O", f"{Fore.LIGHTYELLOW_EX}O{Style.RESET_ALL}").split()[1]}\n'
              f'{" " * 15}{board.replace("X",f"{Fore.LIGHTYELLOW_EX}X{Style.RESET_ALL}").replace("O", f"{Fore.LIGHTYELLOW_EX}O{Style.RESET_ALL}").split()[2]}\n'
              f'{"-" * 37}')


def score_display(x_wins, o_wins):
    print(f'{" " * 15}Score:\n'
          f'{" " * 15}{x}: {x_wins}\n'
          f'{" " * 15}{o}: {o_wins}\n'
          f'{"-" * 37}')


def first_move(flag):
    if flag:
        print(f'{"-" * 37}\n'
              f'{Fore.RED}{"First move belongs to X!" : ^37}{Style.RESET_ALL}\n'
              f'{"-" * 37}')
    else:
        print(f'{"-" * 37}\n'
              f'{Fore.GREEN}{"First move belongs to O!" : ^37}{Style.RESET_ALL}\n'
              f'{"-" * 37}')


def game_over(winner):
    if winner == 'x':
        print(f'{"-"*37}\n'
                      f'{Fore.RED}{"X Victory!" : ^37}{Style.RESET_ALL}\n'
                      f'{"-"*37}')
    elif winner == 'o':
        print(f'{"-"*37}\n'
                      f'{Fore.GREEN}{"O Victory!" : ^37}{Style.RESET_ALL}\n'
                      f'{"-"*37}')
    else:
        print(f'{"-" * 37}\n'
                      f'{Fore.LIGHTYELLOW_EX}{"Draw!" : ^37}{Style.RESET_ALL}\n'
                      f'{"-" * 37}')