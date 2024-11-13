def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        parsed_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            parsed_word += char
        answer.append(parsed_word)
    
    return ' '.join(answer)