arr = list(map(int, input().split()))

is_sorted = True
temp = -1000000
for num in arr:
    if num >= temp:
        temp = num
    else:
        is_sorted = False
        break

if is_sorted:
    print('Good')
else:
    print('Bad')