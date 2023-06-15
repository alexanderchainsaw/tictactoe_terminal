from colorama import Fore, Style
from random import getrandbits
from time import sleep

from functions import won, board_display, score_display, first_move, game_over

yellow = Fore.LIGHTYELLOW_EX
green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL


def main():
    board = '1-2-3\n4-5-6\n7-8-9'
    x_victories = 0
    o_victories = 0
    moves = 0
    available_moves = '123456789'
    flag = bool(getrandbits(1))
    print(f'{"Flipping a coin..." : ^37}')
    sleep(1.5)
    first_move(flag)
    board_display(board)

    while True:
        if flag:
            x_move = input(f'Place X at the position({red}{available_moves}{reset}): ').lower()
            if x_move not in available_moves or len(x_move) > 1:
                print('Invalid position. Try again.')
                continue
            board = board.replace(x_move, 'X')
            moves += 1
            available_moves = available_moves.replace(x_move, '')
            if won(board):
                board_display(board)
                game_over('x')
                if moves == 9:
                    print(f'{Fore.BLUE}{"DOUBLE WIN!!!" : ^37}{Style.RESET_ALL}')
                    x_victories += 1
                x_victories += 1
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    flag = False
                    moves = 0
                    continue
                else:
                    break
            if moves == 9:
                board_display(board, draw=True)
                game_over('draw')
                x_victories += 0.5
                o_victories += 0.5
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    moves = 0
                    flag = False
                    continue
                else:
                    break
            board_display(board)
            flag = False
        else:
            o_move = input(f'Place O at the position({green}{available_moves}{reset}): ').lower()
            if o_move not in available_moves or len(o_move) > 1:
                print('Invalid position. Try again.')
                continue
            board = board.replace(o_move, 'O')
            moves += 1
            available_moves = available_moves.replace(o_move, '')
            if won(board):
                board_display(board)
                game_over('o')
                if moves == 9:
                    print(f'{Fore.BLUE}{"DOUBLE WIN!!!" : ^37}{Style.RESET_ALL}')
                    o_victories += 1
                o_victories += 1
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    moves = 0
                    flag = True
                    continue
                else:
                    break
            if moves == 9:
                board_display(board, draw=True)
                game_over('draw')
                x_victories += 0.5
                o_victories += 0.5
                score_display(x_victories, o_victories)
                if input("Play again?(Y/N): ").lower() == 'y':
                    board = '1-2-3\n4-5-6\n7-8-9'
                    board_display(board)
                    available_moves = '123456789'
                    moves = 0
                    flag = True
                    continue
                else:
                    break
            board_display(board)
            flag = True

            
if __name__ == '__main__':
    main()
