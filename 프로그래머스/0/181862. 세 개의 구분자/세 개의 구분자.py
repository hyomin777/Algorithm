def solution(myStr):
    splited = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split(' ')
    answer = []
    for string in splited:
        if string != "":
            answer.append(string)
            
    if not answer:
        return ["EMPTY"]
    return answer