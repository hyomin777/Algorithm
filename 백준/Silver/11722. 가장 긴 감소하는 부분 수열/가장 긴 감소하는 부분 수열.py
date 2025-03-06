N = int(input())
arr = list(map(int, input().split()))
X = [arr[0]]


def binary_search(X, target):
    start, end = 0, len(X)-1

    while start < end:
        mid = (start + end) // 2

        if X[mid] <= target:
            end = mid
        else:
            start = mid + 1

    return end


for i in range(1, N):
    if X[-1] > arr[i]:
        X.append(arr[i])
    else:
        idx = binary_search(X, arr[i])
        X[idx] = arr[i]

print(len(X))
