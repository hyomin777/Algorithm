def solution(n, control):
    dict = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10
    }
    
    for key in control:
        n += dict[key]
        
    return n