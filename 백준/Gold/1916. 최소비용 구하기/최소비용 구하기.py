import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    v, u, w = map(int, input().split())
    graph[v].append((u, w))

start, end = map(int, input().split())

heap = [(0, start)]
distances = [float('inf')] * (N+1)
distances[start] = 0
visited = [False] * (N+1)

while heap:
    _, current = heappop(heap)
    if visited[current]:
        continue
    visited[current] = True

    for node, weight in graph[current]:
        if distances[current] + weight < distances[node]:
            distances[node] = distances[current] + weight
            heappush(heap, (distances[node], node))
    
print(distances[end])