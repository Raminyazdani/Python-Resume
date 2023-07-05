import copy
import itertools
import os
import random

import keyboard

board_last = []

def remove_zeroes(board, key_pressed):
    if key_pressed in ["w", "s"]:
        for j in range(len(board)):
            temp = []
            temp_0 = []
            for i in range(len(board)):
                if board[i][j] != 0:
                    temp.append(board[i][j])
                else:
                    temp_0.append(0)
            if key_pressed == "w":
                temp = temp + temp_0
            else:
                temp = temp_0 + temp
            for i in range(len(board)):
                board[i][j] = temp[i]

    elif key_pressed in ["a", "d"]:
        for i in range(len(board)):
            temp = []
            temp_0 = []
            for j in range(len(board)):
                if board[i][j] != 0:
                    temp.append(board[i][j])
                else:
                    temp_0.append(0)
            if key_pressed == "a":
                temp = temp + temp_0
            else:
                temp = temp_0 + temp
            board[i] = temp

    return board

def game_logic(board, key_pressed):
    if key_pressed in ["w", "s", "a", "d"]:
        if key_pressed == "s":
            board = board[::-1]
        elif key_pressed == "a":
            board = [list(reversed(col)) for col in zip(*board)]

        elif key_pressed == "d":
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]) - 1,
                                                                             -1,
                                                                             -1)]

        for j in range(len(board)):
            while True:
                temp_col_org = []
                for i in range(len(board)):
                    temp_col_org.append(board[i][j])
                temp_col = temp_col_org.copy()
                for i in range(1,
                               len(temp_col)):
                    if temp_col[i] == temp_col[i - 1]:
                        temp_col[i - 1] = temp_col[i] * 2
                        temp_col[i] = 0
                    elif temp_col[i - 1] == 0:
                        temp_col[i - 1] = temp_col[i]
                        temp_col[i] = 0
                for i in range(len(board)):
                    board[i][j] = temp_col[i]
                if temp_col == temp_col_org:
                    break
        if key_pressed == "s":
            board = board[::-1]
        elif key_pressed == "a":
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]) - 1,
                                                                             -1,
                                                                             -1)]
        elif key_pressed == "d":
            board = [list(reversed(col)) for col in zip(*board)]
        else:
            board = board
    else:
        print_board(board,
                    "Please enter a valid key")

    return board

def get_board(num: int = 4):
    # return a board with num*num positions
    return [[0 for _ in range(num)] for _ in range(num)]

def print_board(board: list, msg: str = ""):
    # print a board
    os.system("cls")
    print(msg)
    try:

        for row in board:
            temp = [str(x) for x in row]
            [print(f"{x:^5s}",end = " ") if x!="0" else print(" --- ",end = " ") for x in temp]
            print()
    except:
        pass

def get_0_positions(board):
    # return a list of positions of 0
    positions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                positions.append((i, j))
    return positions

def get_random_position(positions):
    return random.choice(positions)

message = ""

def no_move(board):
    temp = copy.deepcopy(board)
    cond = True
    for c in ["w","s","d","a"]:
        temp_board = game_logic(temp,c)
        if temp_board !=temp:
            cond = False

    return cond


def game_round(board: list):
    # get zero position
    print_board(board)
    init_board = copy.deepcopy(board)

    # user input (w/s/a/d)
    while True:
        key_pressed = ""
        while True:
            key_pressed = keyboard.read_key()
            if key_pressed in ['w', 's', 'a', 'd', "esc"]:
                break
            else:
                print_board(board,
                            "Please enter a valid key")

        if key_pressed == "esc":
            return False


        # logic of user input
        else:
            board = game_logic(board,
                               key_pressed)

        if init_board == board:
            if no_move(board):
                return False
            continue
        else:
            break
    zeroes = get_0_positions(board)
    zer_pos = get_random_position(zeroes)
    board[zer_pos[0]][zer_pos[1]]=2

    return board  # get zero positions  # select one random zero position  # put 2 in one of the zero positions

if __name__ == '__main__':
    while True:
        dimension = input("Enter the dimension of the board (num*num) only num : ")
        try:
            board = get_board(int(dimension))
            break
        except:
            print("Please enter a valid number")
    zeroes = get_0_positions(board)
    random_zero_position = get_random_position(zeroes)
    board[random_zero_position[0]][random_zero_position[1]] = 2

    while True:
        board = game_round(board)
        if board == False:
            print("Game Over")
            break
