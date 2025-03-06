import sys 
from collections import defaultdict

input = sys.stdin.readline
N =  int(input())

graph = [[0] * N for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        graph[i][j] = arr[j]

for m in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][m] == 1 and graph[m][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(' '.join(list(map(str, row))))
