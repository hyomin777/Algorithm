T = int(input())

words = set()
for _ in range(T):
    word = input()
    words.add(word)

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)