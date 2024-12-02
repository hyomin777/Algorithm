def solution(age):
    answer = ''
    
    for num in str(age):
        answer += chr(int(num) + ord('a'))
        
    return answer
