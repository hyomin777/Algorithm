def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    for char in s:
        if char.upper() == "P":
            p_cnt += 1
        elif char.upper() == "Y":
            y_cnt += 1
            
    return p_cnt == y_cnt