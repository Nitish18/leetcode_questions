from typing import List

class Solution:
    
    def __init__(self):
        self.chess_board = []
        self.chess_board_patterns = []
        
    def create_chess_board(self, n):
        chess_board_grid = []
        for row in range(n):
            tmp = []
            for col in range(n):
                tmp.append(True)
            chess_board_grid.append(tmp)
        self.chess_board = chess_board_grid
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        self.create_chess_board(n)
        ans = self.NQueen(n, 0)
        return self.chess_board_patterns
    
    def NQueen(self, n, row):
        if n == 0:
            self.store_chess_board_pattern()
        for queen in range(row, len(self.chess_board)):
            for j in range(0, len(self.chess_board)):
                if self.isSafeSquare(queen,j):
                    self.updateGrid(queen, j, False)
                    tmp = self.NQueen(n-1, row+1)
                    if not tmp:
                        self.updateGrid(queen, j, True)
                else:
                    continue
            return False
        
    def isSafeSquare(self, i, j):
        for tmp in self.chess_board[i]:
            if tmp == False:
                return False
        for tmp in range(len(self.chess_board)):
            if self.chess_board[tmp][j] == False:
                return False
        # checking both diagonals
        for row in range(len(self.chess_board)):
            for col in range(len(self.chess_board)):
                if row+col == i+j and self.chess_board[row][col]==False:
                    return False
                if col-row == j-i and self.chess_board[row][col]==False:
                    return False
        return True

    def updateGrid(self, i, j, val):
        self.chess_board[i][j] = val

    def store_chess_board_pattern(self):
        tmp = []
        for row in self.chess_board:
            tmp_ste = ""
            for item in row:
                if item == False:
                    tmp_ste = tmp_ste + 'Q'
                else:
                    tmp_ste = tmp_ste + '.'
            tmp.append(tmp_ste)
        self.chess_board_patterns.append(tmp)
