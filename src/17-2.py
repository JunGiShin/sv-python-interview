from typing import List

def wallsAndGates(self, rooms: List[List[int]]) -> None:
    if not rooms:
        return []
    row = len(rooms)
    col = len(rooms[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, dis):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and rooms[nx][ny] > rooms[x][y]:
                rooms[nx][ny] = dis + 1
                dfs(nx, ny, dis + 1)

    for x in range(row):
        for y in range(col):
            if rooms[x][y] == 0:
                dfs(x, y, 0)
