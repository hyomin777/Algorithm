import sys


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())

    stickers = []
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for col in range(1, N):
        if 0 <= col-2:
            dp[0][col] = max(dp[1][col-1]+stickers[0][col], dp[0][col-2]+stickers[0][col], dp[1][col-2]+stickers[0][col])
            dp[1][col] = max(dp[0][col-1]+stickers[1][col], dp[0][col-2]+stickers[1][col], dp[1][col-2]+stickers[1][col])
        else:
            dp[0][col] = dp[1][col-1]+stickers[0][col]
            dp[1][col] = dp[0][col-1]+stickers[1][col]

    print(max(dp[0][-1], dp[1][-1]))