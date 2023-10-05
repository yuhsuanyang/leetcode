# no. 37
class Solution:
    def solveSudoku(self, board) -> None:
        candidates = {}
        nums = [str(i) for i in range(1, 10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candidates[(i, j)] = []
        for i, j in candidates:
            row = self.get_row(board, i)
            col = self.get_col(board, j)
            cell = self.get_cell(board, i, j)
            for k in nums:
                if k not in row+col+cell:
                    candidates[(i, j)].append(k)
        return candidates

    def get_row(self, board, i):
        return board[i]
    
    def get_col(self, board, i):
        return [board[j][i] for j in range(len(board))]

    def get_cell(self, board, i, j):
        if i <= 2:
            cell = [self.get_row(board, k) for k in range(0, 3)]
        elif i > 2 and i <= 5:
            cell = [self.get_row(board, k) for k in range(3, 6)]
        else:
            cell = [self.get_row(board, k) for k in range(6, 9)]
            
        if j <= 2:
            cell = [self.get_col(cell, k) for k in range(0, 3)]
        elif j > 2 and j <=5:
            cell = [self.get_col(cell, k) for k in range(3, 6)]
        else:
            cell = [self.get_col(cell, k) for k in range(6, 9)]
        return sum(cell, [])


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.solveSudoku(board))
#print(sol.get_cell(board, 0, 2))
