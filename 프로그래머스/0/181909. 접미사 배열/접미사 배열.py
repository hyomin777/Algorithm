def solution(my_string):
    answer = []
    string = ''
    
    for char in my_string[::-1]:
        string = char+string
        answer.append(string)
        
    return sorted(answer)