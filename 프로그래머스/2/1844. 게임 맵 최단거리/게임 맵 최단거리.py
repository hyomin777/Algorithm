from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    return -1
