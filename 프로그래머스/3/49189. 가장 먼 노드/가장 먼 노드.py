from collections import defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    
    queue = [1]
    
    while queue:
        node = queue.pop(0)
        current_distance = distances[node]
        
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    
    max_distance = max(distances)

    return distances.count(max_distance)
