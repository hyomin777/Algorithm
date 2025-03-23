def solution(myString):
    answer = []
    splited_string = myString.split('x')
    
    for string in splited_string:
        answer.append(len(string))
    
    return answer