def solution(k, score):
    answer = []
    hall = []
    
    for s in score:
        if len(hall) < k:
            hall.append(s)
            
        elif s > hall[k-1]:
            hall[k-1] = s
            
        hall.sort(reverse=True)            
        answer.append(min(hall))
        
    return answer