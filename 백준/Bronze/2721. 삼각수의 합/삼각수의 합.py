import sys

input = sys.stdin.readline

num_test = int(input())

def T(n):
    return sum([i for i in range(1, n+1)])

def W(n):
    return sum([i * T(i+1) for i in range(1, n+1)])


for _ in range(num_test):
    print(W(int(input())))