class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range (n)]
        result = []
        self.backtrack(board, 0, result)
        return result
    
    def backtrack(self, board, row, result):
        if row == len(board):
            # temp = []
            # for row in board:
            #     temp.append("".join(row))
            # result.append(temp)
            result.append(board.copy())
            return
        
        cols = len(board[row])
        for col in range(cols):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = "Q"
            self.backtrack(board, row + 1, result)
            board[row][col] = "."
    
    def is_valid(self, board, row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False
            
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False
            
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
            if board[i][j] == "Q":
                return False
        return True