import sys

N, M = map(int, sys.stdin.readline().split())

poketmon_dict = {}
poketmons = ['']

for i in range(1, N + 1):
    poketmon = sys.stdin.readline().strip()
    poketmons.append(poketmon)
    poketmon_dict[poketmon] = i 

for _ in range(M):
    question = sys.stdin.readline().strip()

    if question.isdigit():
        print(poketmons[int(question)])
    else:
        print(poketmon_dict[question])
