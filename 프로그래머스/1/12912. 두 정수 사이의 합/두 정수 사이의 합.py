def solution(a, b):
    if a == b:
        return a
    
    answer = 0
    bigger = max(a, b)
    smaller = min(a, b)
    
    for num in range(smaller, bigger+1):
        answer += num
    
    return answer