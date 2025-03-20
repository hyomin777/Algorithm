def solution(strArr):
    answer = []
    for i, word in enumerate(strArr):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer