def find_network(computers, is_visited, idx):
    stack = [idx]
    while stack:
        current = stack.pop()
        
        for idx, computer in enumerate(computers[current]):
            if computer and not is_visited[idx]:
                stack.append(idx)
                is_visited[idx] = True

    return is_visited

def solution(n, computers):
    answer = 0
    is_visited = {i: False for i in range(n)}
            
    for i in range(n):
        if not is_visited[i]:
            is_visited = find_network(computers, is_visited, i)
            answer += 1

    return answer