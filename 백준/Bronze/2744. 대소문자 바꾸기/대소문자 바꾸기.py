word = input()
result = ""

for char in word:
    if char.lower() == char:
        result += char.upper()
    else:
        result += char.lower()

print(result)