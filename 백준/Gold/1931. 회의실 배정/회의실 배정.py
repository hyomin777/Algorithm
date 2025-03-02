import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    arr.append([start, end])

arr.sort(key=lambda x: (x[1], x[0]))
cnt = 0
end_time = 0

for start, end in arr:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)