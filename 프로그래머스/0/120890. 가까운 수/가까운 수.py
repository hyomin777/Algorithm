def solution(array, n):
    answer = 0
    differ = float('inf')
    
    for num in array:
        if abs(n - num) == differ:
            answer = min(num, answer)
            
        elif abs(n - num) < differ:
            differ = abs(n - num)
            answer = num
            
    return answer