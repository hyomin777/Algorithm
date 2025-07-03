def solution(array, height):
    array.sort()
    for idx, value in enumerate(array):
        if value > height:
            return len(array) - idx
    return 0