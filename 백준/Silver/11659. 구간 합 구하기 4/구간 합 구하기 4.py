import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
pre = [0]
sum = 0

for num in arr:
    sum += num
    pre.append(sum)


for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(pre[j] - pre[i-1])
