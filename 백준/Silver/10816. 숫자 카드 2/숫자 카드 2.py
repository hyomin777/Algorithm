import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = Counter(list(map(int, input().split())))


M = int(input())
targets = list(map(int, input().split()))

output = []
for target in targets:
    num_target = cards.get(target)
    if num_target is None:
        output.append(0)
    else:
        output.append(num_target)

print(' '.join(list(map(str, output))))