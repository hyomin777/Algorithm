import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = []
for _ in range(n):
    row = list(map(int, list(str(sys.stdin.readline().strip()))))
    maze.append(row)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

print(maze[n-1][m-1])