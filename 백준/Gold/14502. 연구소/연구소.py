import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())

lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))

walls = []
queue = deque()
num_wall = 3
for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 0:
            walls.append((i, j))
        elif lab[i][j] == 2:
            queue.append((i, j))
        else:
            num_wall += 1

wall_combinations = []
for i in combinations(walls, 3):
    wall_combinations.append(i)

min_cnt = N*M
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for combination in wall_combinations:
    curr_cnt = 0
    copy_lab = deepcopy(lab)
    copy_queue = deepcopy(queue)
    for x, y in combination:
        copy_lab[x][y] = 1

    while copy_queue:
        x, y = copy_queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and copy_lab[nx][ny] == 0:
                curr_cnt += 1
                copy_lab[nx][ny] = 2
                copy_queue.append((nx, ny))
    
    min_cnt = min(min_cnt, curr_cnt)

print(N*M-num_wall-min_cnt-len(queue))
