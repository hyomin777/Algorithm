from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    
    if direction == "right":
        num = queue.pop()
        queue.appendleft(num)
        
    else:
        num = queue.popleft()
        queue.append(num)
        
    return list(queue) 