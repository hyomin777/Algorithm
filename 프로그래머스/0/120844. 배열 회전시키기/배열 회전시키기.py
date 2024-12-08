from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    
    if direction == "right":
        queue.appendleft(queue.pop())
        
    else:
        queue.append(queue.popleft())
        
    return list(queue) 