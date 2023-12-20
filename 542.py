from queue import Queue


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        q = Queue()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.put((i, j))
                else:
                    mat[i][j] = - 1
        
        while not q.empty():
            node_row, node_col = q.get()
            for r, c in directions:
                cur_row = node_row + r
                cur_col = node_col + c
                if cur_row < 0 or cur_row == n or cur_col == m or cur_col < 0 or mat[cur_row][cur_col] != -1:
                    continue
                mat[cur_row][cur_col] = mat[node_row][node_col] + 1
                q.put((cur_row, cur_col))
                
        return mat
