class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range (n)]
        result = []
        self.backtrack(board, 0, result)
        return result
    
    def backtrack(self, board, row, result):
        # 满足结束条件：超过棋盘最后一行
        if row == len(board):
            # 整张放置好皇后的棋盘放入结果列表
            result.append(board.copy())
            return
        
        cols = len(board[row])
        # 选择列表：第 row 行的所有列都是放置皇后的选择
        for col in range(cols):
            # 检查board[row][col]位置是否可以选择放置皇后
            if not self.is_valid(board, row, col):
                continue
            # 做选择，放置皇后
            board[row][col] = "Q"
            # 进入下一层row做多叉树选择
            self.backtrack(board, row + 1, result)
            # 撤销选择，移除皇后
            board[row][col] = "."
    
    def is_valid(self, board, row, col):
        # 检查board[row][col]的正上方
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # 检查board[row][col]的左上方
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False
        # 检查board[row][col]的右上方    
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
            if board[i][j] == "Q":
                return False
        return True