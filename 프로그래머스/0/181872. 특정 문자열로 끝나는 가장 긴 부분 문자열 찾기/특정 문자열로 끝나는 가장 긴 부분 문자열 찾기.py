def solution(myString, pat):
    answer = ''
    
    for i in range(len(myString)+1):
        if myString[:i].endswith(pat):
            answer = myString[:i]
            
    return answer