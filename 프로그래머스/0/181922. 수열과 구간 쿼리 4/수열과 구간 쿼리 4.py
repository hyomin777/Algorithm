def solution(arr, queries):
    for s, e, k in queries:
        for i, num in enumerate(arr):
            if s <= i <= e and i % k == 0:
                arr[i] += 1
            
    return arr