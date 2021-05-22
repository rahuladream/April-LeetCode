# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int):
        def print_board(board):
            for b in board:
                print (" ".join(b))
        def isSafe(board, point, rc):
            row,col = point

            # check col-wise
            for x in range(rc):
                if board[row][x] == "Q" and (row, x) != point:
                    return False

            # check row-wise
            for y in range(row):
                if board[y][col] == "Q" and (y, col) != point:
                    return False

            # check diagonal
            i = row-1
            j = col-1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q" and (i, j) != point:
                    return False
                i -= 1
                j -= 1

            # check diagonal
            i = row+1
            j = col-1
            while i < rc and j >= 0:
                if board[i][j] == "Q" and (i, j) != point:
                    return False
                i += 1
                j -= 1

            return True

            # check diagonal
            i = row-1
            j = col+1
            while i >= 0 and j < rc:
                if board[i][j] == "Q" and (i, j) != point:
                    return False
                i -= 1
                j += 1

            return True

        paths = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtracking(board, position, n, cnt):
            x,y = position

            board[x][y] = "Q"
            res = 0

            if cnt == n:
                paths.append(["".join(row[:]) for row in board])
                res = 1
            else:
                b = y+1
                for a in range(n):
                    if isSafe (board, (a,b), n):
                        z = backtracking(board, (a,b), n, cnt+1)

            board[x][y] = "."

        
        y = 0

        # pick a queen in a column and position the rest of the queens.
        for x in range(n):
            backtracking(board, (x,y), n, 1)

        return paths