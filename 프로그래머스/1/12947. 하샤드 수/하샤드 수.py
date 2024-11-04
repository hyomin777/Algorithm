def solution(x):
    str_x = str(x)
    num = 0
    
    for char in str_x:
        num += int(char)
    
    return x % num == 0