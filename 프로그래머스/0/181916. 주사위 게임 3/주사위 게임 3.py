from collections import Counter

def solution(a, b, c, d):
    counts = Counter([a, b, c, d])
    keys = list(counts.keys())
    values = list(counts.values())
    
    if len(keys) == 1:
        return 1111 * keys[0]
    
    if len(keys) == 2 and 3 in values:
        p = keys[values.index(3)]
        q = keys[values.index(1)]
        return (10 * p + q) ** 2
    
    if len(keys) == 2 and values.count(2) == 2:
        p, q = keys
        return (p + q) * abs(p - q)
    
    if len(keys) == 3:
        p = keys[values.index(2)]
        q, r = [key for key in keys if key != p]
        return q * r
    
    if len(keys) == 4:
        return min(keys)
