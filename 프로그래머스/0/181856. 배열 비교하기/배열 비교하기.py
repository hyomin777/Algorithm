def solution(arr1, arr2):
    n, m = len(arr1), len(arr2)
    if n > m:
        return 1
    if m > n:
        return -1
    
    n, m = sum(arr1), sum(arr2)
    if n > m:
        return 1
    if m > n:
        return -1 
    
    return 0