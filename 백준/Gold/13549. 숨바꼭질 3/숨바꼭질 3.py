import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

if k <= n:
    print(n-k)

else:
    max_pos = k*2+1
    visited = [False] * max_pos
    visited[n] = True
    queue = deque([(n, 0)])

    while queue:
        current, step = queue.popleft()

        if current == k:
            print(step)
            break

        
        if current * 2 < max_pos and not visited[current*2]:
            visited[current*2] = True
            queue.appendleft((current*2, step))
        
        if current - 1 >= 0 and not visited[current-1]:
            visited[current-1] = True
            queue.append((current-1, step+1))

        if current + 1 < max_pos and not visited[current+1]:
            visited[current+1] = True
            queue.append((current+1, step+1))
