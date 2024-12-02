def solution(intStrs, k, s, l):
    answer = []
    
    for num in intStrs:
        cut = int(num[s:s+l])
        answer.append(cut) if cut > k else None
    return answer