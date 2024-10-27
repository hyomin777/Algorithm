def solution(n):
    if n <= 1:
        return 1
    if n <= 2:
        return 2
    if n <= 3:
        return 4

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        for j in range(1, 4):
            dp[i] += dp[i-j]

    return dp[n]


t = int(input())

for _ in range(t):
    n = int(input())
    print(solution(n))
