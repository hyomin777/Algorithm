def solution(rsp):
    answer = ''
    
    for char in rsp:
        if char == "0":
            answer += "5"
        if char == "2":
            answer += "0"
        if char == "5":
            answer += "2"
            
    return answer