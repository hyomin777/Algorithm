def solution(a, b):
    answer = 0
    
    for a_num, b_num in zip(a, b):
        answer += a_num * b_num
    
    return answer