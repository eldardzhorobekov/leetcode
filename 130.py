class Solution:
    def solve(self, board: List[List[str]]) -> None:
        banned = set()
        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
                return
            if board[i][j] == 'X':
                return
            if (i, j) in banned:
                return
            banned.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for row_idx in range(len(board)):
            if row_idx in (0, len(board) - 1):
                col_idxs = range(len(board[row_idx]))
            else:
                col_idxs = (0, len(board[row_idx]) - 1)
            
            for col_idx in col_idxs:
                dfs(row_idx, col_idx)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in banned:
                    board[i][j] = 'X'




