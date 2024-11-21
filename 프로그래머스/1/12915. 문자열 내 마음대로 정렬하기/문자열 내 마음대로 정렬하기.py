def solution(strings, n):
    answer = []
    words = []
    
    for word in strings:
        words.append([word[n], word])    
    
    words.sort()
    
    for _, word in words:
        answer.append(word)
    return answer