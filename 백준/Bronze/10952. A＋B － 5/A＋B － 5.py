import sys

A, B = 1, 1
while A != 0 and B != 0:
    A, B = map(int, sys.stdin.readline().split())
    if A != 0 and B != 0:
        print(A + B)