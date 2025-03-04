import sys

N = int(sys.stdin.readline())
A, B, C = map(int, sys.stdin.readline().split())

A = min(A, N)
B = min(B, N)
C = min(C, N)
print(A+B+C)