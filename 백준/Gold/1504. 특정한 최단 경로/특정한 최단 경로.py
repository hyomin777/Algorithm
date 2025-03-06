import sys
from collections import defaultdict, deque

input = sys.stdin.readline

V, E = map(int, input().split())

graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v_1, v_2 = map(int, input().split())

def dijkstra(graph, start):
    queue = deque([start])
    distances = [float('inf')] * (V+1)
    distances[start] = 0

    while queue:
        curr = queue.popleft()

        for node, weight in graph[curr]:
            if distances[curr] + weight < distances[node]:
                distances[node] = distances[curr] + weight
                queue.append(node)
    
    return distances

distances_from_start = dijkstra(graph, 1)
distances_from_v_1 = dijkstra(graph, v_1)
distances_from_v_2 = dijkstra(graph, v_2)
v1_val = distances_from_start[v_1] + distances_from_v_1[v_2] + distances_from_v_2[V]
v2_val = distances_from_start[v_2] + distances_from_v_2[v_1] + distances_from_v_1[V]

if v1_val + v2_val < float('inf'):
    print(min(v1_val, v2_val))
else:
    print(-1)