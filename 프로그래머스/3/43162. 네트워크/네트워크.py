from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            queue = deque([i])
            visited[i] = True
            
            while queue:
                node = queue.popleft()

                for neighbor in range(n):
                    if computers[node][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    return answer
