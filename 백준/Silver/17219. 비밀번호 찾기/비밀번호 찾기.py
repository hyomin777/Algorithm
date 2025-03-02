n, m = map(int, input().split())

dict = {}
for _ in range(n):
    address, password = input().split()
    dict[address] = password

for _ in range(m):
    print(dict[input()])