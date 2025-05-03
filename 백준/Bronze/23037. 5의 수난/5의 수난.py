num = str(input())

result = 0
for char in num:
    result += int(char) ** 5

print(result)
