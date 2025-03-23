import numpy as np

def solution(arr, k):
    arr = np.array(arr)
    
    if k % 2 == 0:
        arr = arr + k
    else:
        arr = arr * k
    
    return arr.tolist()