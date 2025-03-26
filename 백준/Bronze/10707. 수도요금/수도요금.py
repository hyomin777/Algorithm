import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())


X = A * P

extra = 0
if C < P:
    extra = (P-C) * D

Y = B + extra

print(min(X, Y))