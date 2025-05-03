dict = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16,
    'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
}

t = int(input())

for _ in range(t):
    life = str(input())
    score = 0
    for char in life:
        score += dict.get(char, 0)
    
    if score == 100:
        print("PERFECT LIFE")
    else:
        print(score)