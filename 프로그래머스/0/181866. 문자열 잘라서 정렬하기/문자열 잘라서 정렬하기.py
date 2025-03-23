def solution(myString):
    answer = []
    split = ''
    for string in myString:
        if string == 'x' and len(split) > 0:
            answer.append(split)
            split = ''
        elif string != 'x':
            split += string
            
    if len(split) > 0:
        answer.append(split)
    
    return sorted(answer)