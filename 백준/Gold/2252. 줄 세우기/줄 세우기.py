import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
indegree = [0] * (N+1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

queue = deque()
for node in range(1, N+1):
    if indegree[node] == 0:
        queue.append(node)

result = []
while queue:
    curr = queue.popleft()
    result.append(curr)

    for neighbor in graph[curr]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

print(' '.join(list(map(str, result))))
