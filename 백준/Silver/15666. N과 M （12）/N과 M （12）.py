import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

exist = set()
def dfs(idx, stack):
    if len(stack) == M:
        stack = tuple(stack)
        if stack not in exist:
            exist.add(stack)
            print(' '.join(map(str, stack)))
        return
    
    for i in range(idx, N):
        stack.append(numbers[i])
        dfs(i, stack)
        stack.pop()

dfs(0, [])