import sys

input = sys.stdin.readline
N = int(input())
arr = [0]
for num in list(map(int, input().split())):
    arr.append(num)
dp = [0] * (N+1)

for i in range(N+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
