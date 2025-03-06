import sys
from collections import defaultdict

input = sys.stdin.readline

V = int(input())
E = int(input())

graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distances = [[float('inf')] * (V+1) for _ in range(V+1)]
for curr in graph:
    for node, weight in graph[curr]:
        distances[curr][node] = min(distances[curr][node], weight)

for m in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if distances[i][m] + distances[m][j] < distances[i][j]:
                distances[i][j] = distances[i][m] + distances[m][j]

for i in range(1, V+1):
    distances[i][i] = 0
    for j in range(1, V+1):
        if distances[i][j] == float('inf'):
            distances[i][j] = 0

for row in distances[1:]:
    print(' '.join(list(map(str, row[1:]))))