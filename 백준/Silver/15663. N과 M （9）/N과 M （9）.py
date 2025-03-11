import sys 

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
exists = set()

def dfs(stack, visited):
    if len(stack) == M:
        stack = tuple(stack)
        if stack not in exists:
            print(' '.join(list(map(str, stack))))
            exists.add(stack)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(numbers[i])
            dfs(stack, visited)
            stack.pop()
            visited[i] = False

dfs([], [False] * (N+1))