from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [[0,1], [2,1], [0, 2]]
        0: [1, 2]
        1: []
        2: [1]
        """
        visiting = set()
        visited = set()
        courses_id_to_dependants = defaultdict(set)
        for a, b in prerequisites:
            courses_id_to_dependants[a].add(b)
        
        def dfs(idx: int) -> bool:
            if idx in visiting:
                return False
            if idx in visited:
                return True
            
            visiting.add(idx)
            for course_id in courses_id_to_dependants[idx]:
                if not dfs(course_id):
                    return False

            visiting.remove(idx)
            visited.add(idx)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

