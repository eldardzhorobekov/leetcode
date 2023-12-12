class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(row_id: int) -> None:
            if row_id in visited:
                return
            visited.add(row_id)
            for idx, elem in enumerate(isConnected[row_id]):
                if elem == 1:
                    dfs(idx)
        
        visited = set()
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans

