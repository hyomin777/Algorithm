import numpy as np

def solution(array):
    max_idx = np.argmax(np.array(array))
    return [array[max_idx], int(max_idx)]