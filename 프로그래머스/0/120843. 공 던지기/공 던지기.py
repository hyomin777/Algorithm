def solution(numbers, k):
    n = (k-1) * 2
    return n % len(numbers) + 1