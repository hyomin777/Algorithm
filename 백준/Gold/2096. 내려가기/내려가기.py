import sys 

input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

prev_max = arr[0][:]
prev_min = arr[0][:]

for row in range(1, N):
    curr_max = [0] * 3
    curr_min = [0] * 3

    for col in range(3):
        left = prev_max[col-1] if col > 0 else 0
        middle = prev_max[col]
        right = prev_max[col+1] if col < 2 else 0

        curr_max[col] = arr[row][col] + max(left, middle, right)

        left = prev_min[col-1] if col > 0 else float('inf')
        middle = prev_min[col]
        right = prev_min[col+1] if col < 2 else float('inf')

        curr_min[col] = arr[row][col] + min(left, middle, right)

    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))
