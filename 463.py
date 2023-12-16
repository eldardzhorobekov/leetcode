class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check(i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return 0
            if grid[i][j] == 0:
                return 0
            return 1

        
        def dfs(i: int, j: int) -> int:
            if grid[i][j] == 0:
                return 0
            res = 4 - (
                check(i + 1, j)
                + check(i - 1, j)
                + check(i, j + 1)
                + check(i, j - 1)
            )
            return res
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
        return ans

