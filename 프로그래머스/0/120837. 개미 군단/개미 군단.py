def solution(hp):
    big = hp // 5
    medium = (hp % 5) // 3
    small = (hp % 5) % 3
    return  big + medium + small