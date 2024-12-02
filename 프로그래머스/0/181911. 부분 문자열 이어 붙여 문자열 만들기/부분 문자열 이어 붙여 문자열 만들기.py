def solution(my_strings, parts):
    answer = []
    
    for i, (s, e) in enumerate(parts):
        answer.append(my_strings[i][s:e+1])
        
    return ''.join(answer)