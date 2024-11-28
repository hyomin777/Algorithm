def can_change(word, target):
    cnt = 0
    
    for char1, char2 in zip(word, target):
        if char1 != char2:
            cnt += 1
            
    return cnt == 1

def solution(begin, target, words):
    queue = [(begin, 0)]
    is_visited = set([begin])
    
    while queue:
        current, cnt = queue.pop(0)
        
        if current == target:
            return cnt
        
        for word in words:
            if can_change(current, word) and word not in is_visited:
                queue.append((word, cnt+1))
                is_visited.add(word)
                
    return 0