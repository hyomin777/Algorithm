def solution(clothes):
    answer = 1
    dict = {}
    
    for i, j in clothes:
        if not j in dict:
            dict[j] = 1
        else:
            dict[j] += 1
            
    for key in dict:
        answer *= dict[key] + 1
        
    return answer - 1
        