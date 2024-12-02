def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for idx, citation in enumerate(citations):
        answer = max(answer, min(citation, idx+1))
        
    return answer 