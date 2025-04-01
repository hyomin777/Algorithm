def solution(arr, n): 
    if len(arr) % 2 != 0:
        for idx in range(len(arr)):
            if idx % 2 == 0:
                arr[idx] += n
    else:
        for idx in range(len(arr)):
            if idx % 2 != 0:
                arr[idx] += n
                
    return arr