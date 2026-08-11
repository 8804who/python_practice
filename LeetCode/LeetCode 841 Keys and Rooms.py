from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys = set()
        q = deque()
        
        q.append(0)
        visited.add(0)
        
        while q:
            room = q.popleft()

            for key in rooms[room]:
                keys.add(key)

            for i in keys:
                if i in visited:
                    continue
                q.append(i)
                visited.add(i)

        return len(visited) == len(rooms)