import time


sudoku_board = [
    [0, 0, 0, 1, 0, 0, 0, 9, 0],
    [7, 0, 0, 0, 0, 0, 1, 2, 6],
    [2, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 8, 0, 0, 2, 9, 0, 0],
    [0, 0, 0, 0, 0, 8, 2, 0, 5],
    [9, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 5, 0, 3, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 1, 0]
] 


def draw_board(board):
    for row in range(len(board[0])):
        print()
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(str(board[row][col]) + " ", end="")


def empty_space_finder(board):
    for row in range(9):
        if 0 in board[row]:
            posXofEmpty = board[row].index(0)
            return row, posXofEmpty
    return None


def check_if_can_fit(board, numToCheck, posX, posY):
    if numToCheck in board[posY]:
        return False
    for colToCheck in range(9):
        if board[colToCheck][posX] == numToCheck:
            return False
    square = []
    r = posY // 3
    c = posX // 3
    for row in range(r * 3, r * 3 + 3):
        for col in range(c * 3, c * 3 + 3):
            square.append(board[row][col])
    if numToCheck in square:
        return False
    return True


def solving_magic(board_to_solve):
    location = empty_space_finder(board_to_solve)
    if location is None:
        draw_board(board_to_solve)
        return False
    emptyY, emptyX = location
    for possible_num in range(1, 10):
        if check_if_can_fit(board_to_solve, possible_num, emptyX, emptyY):
            board_to_solve[emptyY][emptyX] = possible_num
            if solving_magic(board_to_solve):
                return True
            board_to_solve[emptyY][emptyX] = 0
    return False


def unnecesary_function():
    print("\n\nSolving magic happening...")
    time.sleep(1)
    print("Still going...")
    time.sleep(1)
    print("Almost there...")
    time.sleep(1)
    print("Done!")

draw_board(sudoku_board)
unnecesary_function()
solving_magic(sudoku_board)
