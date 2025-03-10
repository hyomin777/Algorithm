import sys
from collections import deque, defaultdict


input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    V, U = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

result = [0] * (N+1)

queue = deque([1])
while queue:
    vertex = queue.popleft()

    for neighbor in graph[vertex]:
        if result[neighbor] == 0:
            result[neighbor] = vertex
            queue.append(neighbor)

for parent in result[2:]:
    print(parent)
