import sys

n = int(sys.stdin.readline())
arr = set()

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'add':
        arr.add(command[1])
    elif command[0] == 'remove':
        arr.discard(command[1])
    elif command[0] == 'check':
        if command[1] in arr:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if command[1] in arr:
            arr.remove(command[1])
        else:
            arr.add(command[1])
    elif command[0] == 'all':
        arr.clear()
        arr.update(map(str, range(1, 21)))
    else:
        arr.clear()