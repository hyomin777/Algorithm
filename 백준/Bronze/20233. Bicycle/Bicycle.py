a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

option_a = a + (max(0, T-30) * x) * 21
option_b = b + (max(0, T-45) * y) * 21
print(option_a, option_b)
