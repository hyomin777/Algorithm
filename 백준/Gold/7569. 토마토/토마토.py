import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

box = []
for _ in range(H):
    depth = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        depth.append(row)
    box.append(depth)

queue = deque()
for depth in range(H):
    for row in range(N):
        for col in range(M):
            if box[depth][row][col] == 1:
                queue.append((depth, row, col))

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

while queue:
    z, x, y = queue.popleft()
    for dz, dx, dy in directions:
        nz, nx, ny = z+dz, x+dx, y+dy
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = box[z][x][y] + 1
            queue.append((nz, nx, ny))

def estimate_days(H, N, days):
    for depth in range(H):
        for row in range(N):
            if 0 in box[depth][row]:
                print(-1)
                return
            days = max(days, max(box[depth][row]))
    print(days-1)

estimate_days(H, N, 0)