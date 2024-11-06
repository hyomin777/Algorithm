def solution(phone_number):
    answer = '*' * (len(phone_number) - 4)
    
    for char in phone_number[-4:]:
        answer += char
    return answer