def solution(my_str, n):
    answer = []
    cnt = 0
    alphabet = ''
    
    for char in my_str:
        alphabet += char
        cnt += 1
        if cnt >= n:
            cnt = 0
            answer.append(alphabet)
            alphabet = ''
    if alphabet:
        answer.append(alphabet)
    return answer