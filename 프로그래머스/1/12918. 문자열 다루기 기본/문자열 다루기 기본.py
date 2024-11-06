def solution(s):
    n = len(s)
    
    if n != 4 and n != 6:
        return False
    
    for i in s:
        try:
            int(i)
        except:
            return False
    
    return True