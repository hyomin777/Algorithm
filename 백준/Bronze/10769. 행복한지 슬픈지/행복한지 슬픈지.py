input = input()

happy = 0
sad = 0
for i in range(len(input)-2):
    if input[i:i+3] == ":-)":
        happy += 1
    elif input[i:i+3] == ":-(":
        sad += 1

if happy + sad == 0:
    print("none")
elif happy > sad:
    print('happy')
elif sad > happy:
    print('sad')
else:
    print('unsure')