def solution(n):
    fac = 1
    
    for i in range(1, 3628800):
        fac *= i

        if fac > n:
            return i-1