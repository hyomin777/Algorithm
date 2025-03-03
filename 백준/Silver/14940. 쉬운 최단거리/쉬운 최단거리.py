import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

distances = [[0] * m for _ in range(n)]
maze = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    maze.append(row)

start_x, start_y = None, None
for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            start_x, start_y = i, j
            break
    if start_x is not None:
        break

queue = deque([(start_x, start_y)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
        nx, ny = dx+x, dy+y
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and distances[nx][ny] == 0:
            distances[nx][ny] = distances[x][y] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if maze[i][j] == 1 and distances[i][j] == 0:
            distances[i][j] = -1
    print(' '.join(map(str, distances[i])))

