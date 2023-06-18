import random
from colorama import Fore, Style
from random import getrandbits
from time import sleep

from functions import x, o, won, board_display, score_display, first_move, game_over
from ai_opponent import ai_move

yellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL


def main():
    choosing = True
    pve = False
    while choosing:
        choice = input(f"{'Select mode:' : ^37}\n"
                       f"{green + '(1)' + reset + '.PvP' + red + '(2)' + reset + '.PvE' : ^55}\n")
        if choice == '1':
            choosing = False
        elif choice == '2':
            pve = True
            choosing = False
        else:
            print("Invalid input")
    if pve:
        ai = random.choice('xo')
        if ai == 'x':
            print(f'{"You are playing as " + o + "!" : ^45}')
        else:
            print(f'{"You are playing as " + x + "!" : ^45}')
    else:
        ai = ''
    board = '1-2-3\n4-5-6\n7-8-9'
    x_victories, o_victories = 0, 0
    available_moves = '123456789'
    flag = bool(getrandbits(1))
    print(f'{"Flipping a coin..." : ^37}')
    sleep(1.5)
    first_move(flag)
    board_display(board)

    while True:
        if flag:
            if ai == 'x':
                x_move = ai_move(board, available_moves, 'X', 'O')
                print(f'{"AI places " + x + " at cell " + x_move : ^45}')
            else:
                x_move = input(f'Place X at the position({red}{available_moves}{reset}): ').lower()
                if x_move not in available_moves or len(x_move) > 1:
                    print('Invalid position. Try again.')
                    continue
            board = board.replace(x_move, 'X')
            available_moves = available_moves.replace(x_move, '')
            if won(board):
                board_display(board)
                game_over('x')
                if won(board) == 2:
                    print(f'{Fore.BLUE}{"DOUBLE WIN!!!" : ^37}{Style.RESET_ALL}')
                    x_victories += 1
                x_victories += 1
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    flag = False
                    continue
                else:
                    break
            if not available_moves and not won(board):
                board_display(board, draw=True)
                game_over('draw')
                x_victories += 0.5
                o_victories += 0.5
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    flag = False
                    continue
                else:
                    break
            board_display(board)
            flag = False
        else:
            if ai == 'o':
                o_move = ai_move(board, available_moves, 'O', 'X')
                print(f'{"AI places " + o + " at cell " + o_move : ^45}')
            else:
                o_move = input(f'Place O at the position({green}{available_moves}{reset}): ').lower()
                if o_move not in available_moves or len(o_move) > 1:
                    print('Invalid position. Try again.')
                    continue
            board = board.replace(o_move, 'O')
            available_moves = available_moves.replace(o_move, '')
            if won(board):
                board_display(board)
                game_over('o')
                if won(board) == 2:
                    print(f'{Fore.BLUE}{"DOUBLE WIN!!!" : ^37}{Style.RESET_ALL}')
                    o_victories += 1
                o_victories += 1
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    flag = True
                    continue
                else:
                    break
            if not available_moves and not won(board):
                board_display(board, draw=True)
                game_over('draw')
                x_victories += 0.5
                o_victories += 0.5
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    flag = True
                    continue
                else:
                    break
            board_display(board)
            flag = True

            
if __name__ == '__main__':
    main()
