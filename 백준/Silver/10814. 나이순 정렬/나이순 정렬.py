import sys

input = sys.stdin.readline

N = int(input().strip())

list = []
for i in range(N):
    age, name = input().strip().split()
    age = int(age)
    list.append((age, i, name))

list.sort(key=lambda x: (x[0], x[1]))
for element in list:
    print(element[0], element[2])
    