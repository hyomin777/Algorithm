def solution(my_string, target):
    n = len(target)
    for i in range(len(my_string)-n+1):
        if my_string[i:i+n] == target:
            return 1
    return 0