def solution(my_string):
    answer = 0
    flag = False
    temp = ''
    for char in my_string:
        try:
            num = int(char)
            temp += char
            flag = True
        except:
            if temp:
                answer += int(temp)
            temp = ''
            flag = False
            
    if temp:
        answer += int(temp)
    return answer