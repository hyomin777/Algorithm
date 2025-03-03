import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

box = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    box.append(row)

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0: 
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

days = 0
available = True
for row in box:
    if 0 in row:
        print(-1)
        available = False
        break
    days = max(days, max(row))

if available:
    print(days-1)