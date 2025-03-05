import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())

graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heap = [(0, start)]
distances = [float('inf')] * (V+1)
distances[start] = 0
seen = set()
while heap:
    _, current = heappop(heap)
    if current in seen:
        continue
    seen.add(current)

    for node, weight in graph[current]:
        if distances[current] + weight < distances[node]:
            distances[node] = distances[current] + weight
            heappush(heap, (distances[node], node))
    
for distance in distances[1:]:
    if distance == float('inf'):
        print('INF')
    else:
        print(distance)