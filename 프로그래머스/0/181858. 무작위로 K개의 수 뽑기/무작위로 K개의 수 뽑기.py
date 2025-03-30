def solution(arr, k):
    answer = []
    exists = set()
    
    for num in arr:
        if len(answer) >= k:
            break
        if num in exists:
            continue
        else:
            answer.append(num)
            exists.add(num)
    
    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
            
    return answer