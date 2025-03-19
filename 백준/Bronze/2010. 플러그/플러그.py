import sys

input = sys.stdin.readline

N = int(input())

max_value = 1
for _ in range(N):
    value = int(input())
    max_value += value - 1

print(max_value)
