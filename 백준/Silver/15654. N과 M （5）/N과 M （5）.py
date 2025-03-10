import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(start, stack):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return

    for num in numbers:
        if not num in stack:
            stack.append(num)
            dfs(start, stack)
            stack.pop()

for num in numbers:
    dfs(num, [num])