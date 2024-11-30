def is_five(num):
    if num % 5 != 0:
        return False
    
    num = str(num)
    
    for char in num:
        if char == "5" or char == "0":
            continue
        else:
            return False
            
    return True

def solution(l, r):
    answer = []
    
    for num in range(l, r+1):
        if is_five(num):
            answer.append(num)
            
    return answer if answer else [-1]