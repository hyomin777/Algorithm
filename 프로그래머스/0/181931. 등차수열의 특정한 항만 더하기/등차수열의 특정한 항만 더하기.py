def solution(a, d, included):
    answer = a if included[0] else 0
    temp = a
    
    for i in range(1, len(included)):
        temp += d
        if included[i]:
            answer += temp
            
    return answer