def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        apples = score[i:i + m]
        
        if len(apples) < m:
            break
        
        min_apple = min(apples)
        answer += min_apple * m
        
    return answer
