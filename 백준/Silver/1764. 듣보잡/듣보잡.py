N, M = map(int, input().split())
arr_n = set()
arr_m = set()

for _ in range(N):
    arr_n.add(input())

for _ in range(M):
    arr_m.add(input())

result = sorted(list(arr_n & arr_m))

print(len(result))
for name in result:
    print(name)