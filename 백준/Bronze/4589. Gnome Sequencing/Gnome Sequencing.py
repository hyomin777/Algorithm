import sys

N = int(sys.stdin.readline())

print("Gnomes:")
for _ in range(N):
    A, B, C = map(int, sys.stdin.readline().split())
    if A <= B <= C or C <= B <= A:
        print("Ordered")
    else:
        print("Unordered")