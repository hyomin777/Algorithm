def solution(n):
    str_n = sorted(list(str(n)), reverse=True)
    
    return int(''.join(str_n))