import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    input_data = sys.stdin.readline().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, input_data[1:-1].split(',')))

    reverse_flag = False
    is_error = False

    for func in p:
        if func == 'R':
            reverse_flag = not reverse_flag
        elif func == 'D':
            if not arr:
                is_error = True
                print('error')
                break
            else:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()

    if not is_error:
        if reverse_flag:
            arr.reverse()
        print(f"[{','.join(map(str, arr))}]")
