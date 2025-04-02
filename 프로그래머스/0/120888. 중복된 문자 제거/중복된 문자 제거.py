def solution(my_string):
    filter = set()
    answer = ''
    
    for char in my_string:
        if char not in filter:
            filter.add(char)
            answer += char
            
    return answer