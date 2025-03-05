import sys

arr = []
for _ in range(9):
    arr.append(int(sys.stdin.readline()))

max_num = max(arr)
print(max_num)
print(arr.index(max_num)+1)
