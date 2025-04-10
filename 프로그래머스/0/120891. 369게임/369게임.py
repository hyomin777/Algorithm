def solution(order):
    answer = 0
    
    for char in str(order):
        if int(char) % 3 == 0 and char != '0':
            answer += 1
    return answer