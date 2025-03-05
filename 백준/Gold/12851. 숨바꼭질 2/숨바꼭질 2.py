import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

if K <= N:
    print(N - K)
    print(1)
else:
    max_point = K * 2 + 1
    arr = [-1] * max_point
    queue = deque([N])

    arr[N] = 0 
    cnt = 0 
    found_distance = -1 

    while queue:
        current = queue.popleft()

        if current == K:
            if found_distance == -1: 
                found_distance = arr[current]
                cnt = 1
            elif arr[current] == found_distance:
                cnt += 1
            continue 

        for next_pos in (current * 2, current + 1, current - 1):
            if 0 <= next_pos < max_point:
                if arr[next_pos] == -1 or arr[next_pos] == arr[current] + 1:
                    arr[next_pos] = arr[current] + 1
                    queue.append(next_pos)

    print(arr[K])
    print(cnt)
