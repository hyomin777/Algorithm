def solution(brown, yellow):
    x = yellow
    
    for i in range(1, yellow+1):
        if yellow % i != 0:
            continue
        
        x = yellow // i
    
            
        if (x * 2) + (i * 2) == (brown - 4):
            return [x+2, i+2]