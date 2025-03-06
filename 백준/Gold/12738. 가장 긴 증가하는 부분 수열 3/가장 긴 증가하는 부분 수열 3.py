import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = [arr[0]]

for i in range(1, N):

    if X[-1] < arr[i]:
        X.append(arr[i])
    else:
        idx = bisect_left(X, arr[i])
        X[idx] = arr[i]

print(len(X))
