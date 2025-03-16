import sys
from collections import defaultdict, deque


input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, graph):
    for node in graph:
        graph[node] = sorted(graph[node], reverse=True)

    stack = [start]
    order_of_visit = []

    while stack:
        node = stack.pop()
        if node not in order_of_visit:
            order_of_visit.append(node)

        for neighbor in graph[node]:
            if neighbor not in order_of_visit:
                stack.append(neighbor)
    
    return order_of_visit

def bfs(start, graph):
    for node in graph:
        graph[node] = sorted(graph[node])

    queue = deque([start])
    order_of_visit = []
    
    while queue:
        node = queue.popleft()
        if node not in order_of_visit:
            order_of_visit.append(node)

        for neighbor in graph[node]:
            if neighbor not in order_of_visit:
                order_of_visit.append(neighbor)
                queue.append(neighbor)
    
    return order_of_visit



print(' '.join(map(str, dfs(V, graph))))
print(' '.join(map(str, bfs(V, graph))))