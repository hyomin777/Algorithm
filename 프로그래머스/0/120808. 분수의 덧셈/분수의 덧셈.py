def simplify(numer, denom):
    divisor = 1
    
    for num in range(2, denom+1):
        if numer % num == 0 and denom % num == 0:
            divisor = num
    
    return [numer // divisor, denom // divisor]

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom2 * denom1
    return simplify(numer, denom)