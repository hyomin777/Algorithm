def solution(numLog):
    dict = {
        1: "w",
        -1: "s",
        10: "d",
        -10: "a"
    }
    
    answer = ''
    current = numLog[0]
    for num in numLog[1:]:
        temp = num - current
        answer += dict[temp]
        current = num
        
    return answer