import sys

input = sys.stdin.readline
N, K = map(int, input().split())
    
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)
    
for w_i, v_i in items:
    for w in range(K, w_i - 1, -1):
        dp[w] = max(dp[w], dp[w - w_i] + v_i)
    
print(dp[K])
