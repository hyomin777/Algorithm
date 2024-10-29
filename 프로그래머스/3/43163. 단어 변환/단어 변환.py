from collections import deque

def can_transform(word1, word2):
    diff_count = 0
    
    for a, b in zip(word1, word2):
        if a != b:
            diff_count += 1   
            
    return diff_count == 1

def solution(begin, target, words):
    if not target in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    visited.add(begin)

    while queue:
        current_word, step_count = queue.popleft()

        if current_word == target:
            return step_count
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, step_count + 1))
    
    return 0
