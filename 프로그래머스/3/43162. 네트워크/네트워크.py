from collections import deque

def solution(n, computers):
    answer = 0
    graph = {}
    
    for i, computer in enumerate(computers):
        graph[i+1] = []
        for j, network in enumerate(computer):
            if network == 1 and i != j:
                graph[i+1].append(j+1)
                
    queue = deque([])
    visited = [0] * (n+1)
    
    for i in range(1, n+1):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            queue.append(graph[i])
        
        while queue:
            computers = queue.popleft()
            
            for computer in computers:
                if visited[computer] == 0:
                    visited[computer] = 1
                    queue.append(graph[computer])
    
    return answer