def solution(my_string):
    answer = 0
    
    for char in my_string:
        try:
            answer += int(char)
            
        except:
            pass
        
    return answer