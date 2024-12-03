def solution(my_string):
    count = [0 for _ in range(52)]
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            count[ord(char) - ord('A')] += 1
        if 'a' <= char <= 'z':
            count[ord(char) - ord('a') + 26] += 1
            
    return count
