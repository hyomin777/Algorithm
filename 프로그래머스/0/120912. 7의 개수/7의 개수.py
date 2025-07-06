def solution(array):
    answer = 0
    for num in array:
        for char in str(num):
            if char == '7':
                answer += 1
    return answer