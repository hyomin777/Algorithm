def solution(n):
    answer = 1
    
    for i in range(1, n+1):
        if (answer * 6) % n != 0:
            answer += 1
        else:
            return answer