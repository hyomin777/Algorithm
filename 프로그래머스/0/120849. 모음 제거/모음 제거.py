def solution(my_string):
    arr = ['a', 'e', 'i', 'o', 'u']
    answer = []
    
    for char in my_string:
        if not char in arr:
            answer.append(char)
    
    return ''.join(answer)