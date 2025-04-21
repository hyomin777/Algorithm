def solution(cipher, code):
    answer = ''
    for idx in range(1, len(cipher)+1):
        if idx % code == 0:
            answer += cipher[idx-1]
    return answer