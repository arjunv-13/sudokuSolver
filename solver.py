import time

def solve(board, row, column, start):
    if start and not boardValid(board):
        return False
    if row == 8 and column == 9:
        return board
    elif column == 9:
        return solve(board, row + 1, 0, False)
    if board[row][column] != 0:
        return solve(board, row, column + 1, False)
    test = 1
    while test <= 9:
        if inputValid(row,column, test, board):
            board[row][column] = test
            potential = solve(board, row, column + 1, False)
            if potential:
                return potential
            board[row][column] = 0
        test += 1
    return False


def boardValid(board):
    return rowsValid(board) and columnsValid(board) and boxesValid(board)

def rowsValid(board) -> bool:
    for row in board:
        inRow = set()
        for x in row:
            if x != 0:
                if x not in inRow:
                    inRow.add(x)
                else:
                    return False
    return True

def columnsValid(board) -> bool:
    for i in range(9):
        inColumn = set()
        for row in board:
            if row[i] != 0:
                if row[i] not in inColumn:
                    inColumn.add(row[i])
                else:
                    return False
    return True

def boxesValid(board) -> bool:
    boxes = {}
    for r in range(9):
        for c in range(9):
            box = getBox(r, c)
            x = board[r][c]
            if x != 0:
                if box not in boxes:
                    boxes[box] = {x}
                elif x in boxes[box]:
                    return False
                else:
                    boxes[box].add(x)
                
    return True

def getBox(r, c) -> int:
    rBox = r//3
    cBox = c//3
    return(rBox * 10 + cBox)

def findFirstEmpty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return [r, c]
    return False

def printBoard(board):
    for row in board:
        print(row)

def inputValid(row, column, test, board):
    for x in board[row]:
        if x == test:
            return False
    for r in board:
        if r[column] == test:
            return False
    box = getBox(row, column)
    rBox = box//10
    cBox = box % 10

    for r in range(rBox * 3, rBox * 3 + 3):
        for c in range(cBox * 3, cBox * 3 + 3):
            if board[r][c] == test:
                return False


    return True

unsolvedBoard = [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0] ]

if __name__ == "__main__":
    start = time.time()
    solved = solve(unsolvedBoard, 0, 0, True)

    print(boardValid(solved))
    printBoard(solved)

    end = time.time()
    print(end - start, "seconds")