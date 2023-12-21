from queue import Queue


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        n = len(grid)
        m = len(grid[0])
        visited = set()
        def bfs(i: int, j: int):
            q = Queue()
            q.put((i, j))
            while not q.empty():
                r, c = q.get()
                for i in range(4):
                    dr, dc = r + di[i], c + dj[i]
                    if dr < 0 or dc < 0 or dr >= n or dc >= m:
                        continue
                    if grid[dr][dc] == "0":
                        continue
                    
                    if (dr, dc) not in visited:
                        visited.add((dr, dc))
                        q.put((dr, dc))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    ans += 1
        return ans
