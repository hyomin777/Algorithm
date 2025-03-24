import sys

input = sys.stdin.readline

a_cards = list(map(int, input().split()))
b_cards = list(map(int, input().split()))
a_score = 0
b_score = 0

flag = 'D'
for a, b in zip(a_cards, b_cards):
    if a > b:
        flag = 'A'
        a_score += 3
    elif a < b:
        flag = 'B'
        b_score += 3
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)
if a_score > b_score:
    print('A')
elif b_score > a_score:
    print('B')
else:
    print(flag)
