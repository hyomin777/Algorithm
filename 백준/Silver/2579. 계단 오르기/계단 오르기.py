def solution(n, arr):
    if n <= 1:
        return arr[1]
    if n <= 2:
        return arr[1] + arr[2]

    dp = [0] * (n+1)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

    return dp[n]

n = int(input())

stairs = [0]
for _ in range(n):
    m = int(input())
    stairs.append(m)

print(solution(n, stairs))