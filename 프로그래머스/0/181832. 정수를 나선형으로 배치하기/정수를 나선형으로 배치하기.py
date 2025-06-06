def solution(n):
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1
    num = 2
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0
    
    row = 0
    col = 0
    while num <= n * n:
        dx, dy = direction[direction_idx % 4]
        
        if row+dx >= n or row+dx < 0 or col+dy >= n or col+dy < 0:
            direction_idx += 1
            continue
        
        if answer[row+dx][col+dy] == 0:       
            row += dx
            col += dy
            answer[row][col] = num
            num += 1
        else:
            direction_idx += 1

    return answer