import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

if K <= N:
    print(N-K)

else:
    arr = [-1] * (K*2+1)
    arr[N] = 0
    queue = deque([N])

    while queue:
        current = queue.popleft()
        if current == K:
            print(arr[current])
            break

        if current*2 < K*2+1 and arr[current*2] == -1:
            arr[current*2] = arr[current] + 1
            queue.appendleft(current*2)
        
        if current+1 < K*2+1 and arr[current+1] == -1:
            arr[current+1] = arr[current] + 1
            queue.append(current+1)

        if current-1 >= 0 and arr[current-1] == -1:
            arr[current-1] = arr[current] + 1
            queue.append(current-1)