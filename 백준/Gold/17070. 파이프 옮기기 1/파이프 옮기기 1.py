import sys 

input = sys.stdin.readline
N = int(input())

house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

directions = {
    'row': [(0, 1, 'row'), (1, 1, 'diag')],
    'col': [(1, 0, 'col'), (1, 1, 'diag')],
    'diag': [(0, 1, 'row'), (1, 0, 'col'), (1, 1, 'diag')]
}
stack = [(0, 1, 'row')]
cnt = 0
while stack:
    row, col, direction = stack.pop()

    if row == N-1 and col == N-1:
        cnt += 1
        continue

    for dx, dy, d in directions[direction]:
        nx, ny = row+dx, col+dy
        if 0 <= nx < N and 0 <= ny < N and house[nx][ny] == 0:
            if d == 'diag' and house[nx-1][ny] == 0 and house[nx][ny-1] == 0:
                stack.append((nx, ny, d))
            elif d != 'diag':
                stack.append((nx, ny, d))

print(cnt)