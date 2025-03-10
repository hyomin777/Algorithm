import sys

input = sys.stdin.readline
N, M = map(int, input().split())

output = []

def dfs(start, arr):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for num in range(start, N+1):
        arr.append(num)
        dfs(num, arr)
        arr.pop()

dfs(1, [])
