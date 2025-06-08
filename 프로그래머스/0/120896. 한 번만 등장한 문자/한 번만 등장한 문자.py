def solution(s):
    exist = set()
    seen = []
    
    answer = ''
    for char in s:
        if char not in exist:
            exist.add(char)
        else:
            seen.append(char)
    
    for char in sorted(exist):
        if char not in seen:
            answer += char
            
    return answer