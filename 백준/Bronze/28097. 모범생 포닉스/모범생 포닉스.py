n = int(input())
arr_t = map(int, input().split())

result = 8 * (n-1)
for t in arr_t:
    result += t

day = result // 24
hour = result - (24 * day)
print(day, hour)