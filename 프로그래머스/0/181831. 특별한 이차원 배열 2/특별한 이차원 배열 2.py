import numpy as np

def solution(arr):
    arr = np.array(arr)
    transpose = arr.T
    return int(arr.tolist() == transpose.tolist())