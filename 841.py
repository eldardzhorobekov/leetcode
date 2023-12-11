class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room_idx: int) -> None:
            if visited[room_idx]:
                return
            visited[room_idx] = True
            for key in rooms[room_idx]:
                dfs(key)

        visited = [False] * len(rooms)
        dfs(0)
        return all(visited)
