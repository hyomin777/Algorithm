N, A, B = map(int, input().split())
positive, negative = 1, 1

for _ in range(N):
    positive += A
    negative += B

    if negative > positive:
        positive, negative = negative, positive
    elif negative == positive:
        negative -= 1

print(positive, negative)
