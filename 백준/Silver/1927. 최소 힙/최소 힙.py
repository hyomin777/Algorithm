import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
min_heap = []

for _ in range(N):
    x = int(input().strip())
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0) 
