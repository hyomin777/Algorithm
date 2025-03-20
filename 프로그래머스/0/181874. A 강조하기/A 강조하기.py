def solution(myString):
    answer = ''
    for char in myString:
        if char == "a" or char == "A":
            answer += char.upper()
        else:
            answer += char.lower()
    return answer