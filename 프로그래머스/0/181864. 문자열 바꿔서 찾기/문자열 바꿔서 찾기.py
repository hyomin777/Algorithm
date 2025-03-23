def solution(myString, pat):
    changed_string = ''
    
    for char in myString:
        if char == 'A':
            changed_string += 'B'
        else:
            changed_string += 'A'
            
    return int(pat in changed_string)