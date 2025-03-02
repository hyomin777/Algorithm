import sys
sys.setrecursionlimit(10**6)

a, b, c = map(int, sys.stdin.readline().split())

print(pow(a, b, c))