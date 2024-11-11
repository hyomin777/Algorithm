def find_min(n, m):
    result = 0
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            result = i
    return result

def find_max(n, m):
    result = 1000000
    for i in range((n*m), max(n, m)-1, -1):
        if i % n == 0 and i % m == 0:
            result = i
    return result

def solution(n, m):
    return [find_min(n, m), find_max(n, m)]