def solution(numbers):
    dict = {}
    answer = 0
    
    for i in range(10):
        dict[i] = False
    
    for num in numbers:
        dict[num] = True
    
    for key, value in dict.items():
        if not value:
            answer += key
    return answer