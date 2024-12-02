def solution(n, k):
    answer = 0
    drink = n // 10
    
    return (n * 12000) + ((k - drink) * 2000)