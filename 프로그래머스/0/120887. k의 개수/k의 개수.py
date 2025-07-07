def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        for char in str(num):
            if char == str(k):
                answer += 1
                
    return answer