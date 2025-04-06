def solution(myString):
    answer = ''
    for string in myString:
        if string < 'l':
            string = 'l'
        answer += string
    
    return answer