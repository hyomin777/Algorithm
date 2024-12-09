from itertools import product

def solution(word):
    arr = []
    words = ['A','E','I','O','U']
    
    for i in range(1, 6):
        for j in list(product(words, repeat=i)):
            arr.append(''.join(j))
            
    arr.sort()
    return arr.index(word)+1