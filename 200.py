class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
                return
            if (i, j) in visited:
                return
            if grid[i][j] == "0":
                return
            
            visited.add((i, j))
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        return ans
