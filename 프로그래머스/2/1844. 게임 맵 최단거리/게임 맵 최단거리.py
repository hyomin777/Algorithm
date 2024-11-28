def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x_path = x + dx
                y_path = y + dy
                
                if x_path >= n or x_path < 0 or y_path >= m or y_path < 0:
                    continue
                
                if maps[x_path][y_path] == 1:
                    maps[x_path][y_path] = maps[x][y] + 1
                    queue.append((x_path, y_path))
        
    return maps[-1][-1] if maps[-1][-1] > 1 else -1