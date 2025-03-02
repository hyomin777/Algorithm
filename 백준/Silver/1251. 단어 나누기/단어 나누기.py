word = input()
words = []

def reverse(s):
    return s[::-1]

for i in range(1, len(word) - 1): 
    for j in range(i + 1, len(word)):
        a, b, c = word[:i], word[i:j], word[j:]
        words.append(reverse(a) + reverse(b) + reverse(c))

words.sort()
print(words[0])