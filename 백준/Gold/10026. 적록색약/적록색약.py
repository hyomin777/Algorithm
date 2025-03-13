from collections import deque

N = int(input())

grid = []
rgb_zone = []
color_blindness_zone = []
for _ in range(N):
    grid.append(list(input()))
    rgb_zone.append([0] * N)
    color_blindness_zone.append([0] * N)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque()
cnt = 0

for i in range(N):
    for j in range(N):
        if rgb_zone[i][j] == 0:
            queue.append((i, j, grid[i][j]))
            cnt += 1
        while queue:
            row, col, color = queue.popleft()
            for dx, dy in direction:
                nx, ny = row+dx, col+dy
                if 0 <= nx < N and 0 <= ny < N and rgb_zone[nx][ny] == 0 and color == grid[nx][ny]:
                    rgb_zone[nx][ny] = cnt if rgb_zone[nx][ny] == 0 else 0
                    queue.append((nx, ny, grid[nx][ny]))

blindness_cnt = 0
for i in range(N):
    for j in range(N):
        if color_blindness_zone[i][j] == 0:
            queue.append((i, j, grid[i][j]))
            blindness_cnt += 1
        while queue:
            row, col, color = queue.popleft()
            for dx, dy in direction:
                nx, ny = row+dx, col+dy
                if 0 <= nx < N and 0 <= ny < N and color_blindness_zone[nx][ny] == 0:
                    if color == grid[nx][ny] or (color == 'R' and grid[nx][ny] == 'G') or (color == 'G' and grid[nx][ny] == 'R'):
                        color_blindness_zone[nx][ny] = cnt if color_blindness_zone[nx][ny] == 0 else 0
                        queue.append((nx, ny, grid[nx][ny]))
        
print(cnt, blindness_cnt)