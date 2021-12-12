import numpy as np


def isBingo(board):
    for i in range(5):
        row_neg = (board[i]<0).sum()
        col_neg = (board[:,i]<0).sum()
        if row_neg == 5 or col_neg == 5:
            return True
    return False

def notMarkedSum(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] > -1:
                sum += board[i][j]
    return sum

def main():
    matrix = np.loadtxt("boards.txt", usecols=range(5),dtype=int)
    boards = np.vsplit(matrix, 100)
    nums = np.genfromtxt("numbers.txt", delimiter=",", dtype=int)

    lastBoard = None
    lastNumber = None
    bingoCount = len(boards) # Total amount of bingo boards

    for num in nums:
        for i in range(len(boards)):
            boards[i] = np.where(boards[i] == num, -1, boards[i])
            if boards[i] == "done":
                pass
            elif isBingo(boards[i]):
                bingoCount -= 1
                if bingoCount > 0:
                    boards[i] = "done"
                if bingoCount == 0:
                    lastBoard = boards[i]
                    lastNumber = num
                    break
        else:
            continue
        break

    print(lastNumber)
    print(lastBoard)
    print(notMarkedSum(lastBoard)*lastNumber)

main()