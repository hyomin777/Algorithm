def solution(n, k):
    drink = max(0, n//10)
    
    return (n * 12000) + ((k - drink) * 2000)