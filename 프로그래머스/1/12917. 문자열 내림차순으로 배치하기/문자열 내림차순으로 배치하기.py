def solution(s):
    s_arr = sorted(list(s), reverse=True)
    return ''.join(s_arr)