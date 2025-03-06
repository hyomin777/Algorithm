import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

distances = [float('inf')] * (N+1)
distances[1] = 0

for _ in range(N):
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight

is_available = True
for node in graph:
    for neighbor, weight in graph[node]:
        if distances[node] + weight < distances[neighbor]:
            is_available = False
            break


if is_available:
    for distance in distances[2:]:
        if distance != float('inf'):
            print(distance)
        else:
            print(-1)

else:
    print(-1)