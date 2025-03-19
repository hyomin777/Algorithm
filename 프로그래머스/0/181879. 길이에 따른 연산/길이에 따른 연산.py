def solution(num_list):
    n = len(num_list)
    if n  >= 11:
        return sum(num_list)
    
    answer = 1
    for num in num_list:
        answer = answer * num
    return answer