
def solution(n):
    answer = set()
    
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = n // i
                answer.add(i)
                break
    
    return list(sorted(answer))