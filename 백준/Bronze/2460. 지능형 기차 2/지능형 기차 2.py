import sys

input = sys.stdin.readline

max_person = 0
curr_person = 0
for _ in range(10):
    num_out, num_in = map(int, input().split())

    curr_person -= num_out
    curr_person += num_in

    max_person = max(max_person, curr_person)

print(max_person)
