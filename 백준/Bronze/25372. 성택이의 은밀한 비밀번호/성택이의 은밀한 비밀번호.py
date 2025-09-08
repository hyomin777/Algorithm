t = int(input())

for _ in range(t):
    password = input()
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")