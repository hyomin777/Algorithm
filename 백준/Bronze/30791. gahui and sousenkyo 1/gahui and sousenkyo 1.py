arr = list(map(int, input().split()))

cnt = 0
max_value = max(arr)
for votes in arr:
    if 0 < max_value - votes <= 1000:
        cnt += 1

print(cnt)