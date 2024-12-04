def solution(my_string, indices):
    answer = []
    
    for idx in range(len(my_string)):
        if not idx in indices:
            answer.append(my_string[idx])
        
    return ''.join(answer)
