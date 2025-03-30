def solution(arr):
    square = 1
    
    while square < len(arr):
        square = square * 2

    while len(arr) < square:
        arr.append(0)
    
    return arr