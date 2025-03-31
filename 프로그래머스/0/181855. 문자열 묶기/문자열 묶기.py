def solution(strArr):
    answer = 0
    strArr.sort(key=lambda x: len(x))
    
    n = len(strArr[0])
    curr = 0
    for string in strArr:
        if len(string) == n:
            curr += 1
        else:
            answer = max(answer, curr)
            curr = 1
            n = len(string)
        
    return max(answer, curr)