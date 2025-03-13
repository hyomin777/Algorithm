T = int(input())

for i in range(1,T+1):
    arr = list(input().split())

    output = f'Case #{i}:'
    for char in arr[::-1]:
        output += f" {char}"

    print(output)

