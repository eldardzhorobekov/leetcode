class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0: []
        1: [0]
        2: [0]
        3: [1,2]
        0, 1, 2, 3 
        """
        pr = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            pr[a].add(b)

        visiting = set()
        visited = set()
        ans = []

        def dfs(idx: int) -> None:
            if idx in visiting:
                return False
            if idx in visited:
                return True

            visiting.add(idx)
            for j in pr[idx]:
                if not dfs(j):
                    return False

            visiting.remove(idx)
            visited.add(idx)
            ans.append(idx)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        # print(pr)
        # print(visited)
        # print(visiting)
        return ans

