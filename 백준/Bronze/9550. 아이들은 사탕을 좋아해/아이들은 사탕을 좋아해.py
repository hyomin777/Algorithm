t = int(input())

for _ in range(t):
    kids = 0

    N, K = map(int, input().split())
    candies = list(map(int, input().split()))

    for candy in candies:
        while candy >= K:
            candy -= K
            kids += 1

    print(kids)