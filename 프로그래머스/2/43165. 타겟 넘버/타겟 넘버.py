def recursion(numbers, n, idx, current, target):
    if n <= idx:
        return 1 if current == target else 0
    
    num1 = recursion(numbers, n, idx+1, current+numbers[idx], target)
    num2 = recursion(numbers, n, idx+1, current-numbers[idx], target)
    
    return num1 + num2

def solution(numbers, target):
    return recursion(numbers, len(numbers), 0, 0, target)