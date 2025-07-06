arr = list(map(int, input().split()))

if sum(arr) >= 100:
    print("OK")
else:
    min_value = min(arr)
    min_idx = arr.index(min_value)

    if min_idx == 0:
        print("Soongsil ")
    elif min_idx == 1:
        print("Korea")
    else:
        print("Hanyang")