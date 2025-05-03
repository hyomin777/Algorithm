import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    num = int(input())

    if num % 2 == 0:
        print('even')
    else:
        print('odd')