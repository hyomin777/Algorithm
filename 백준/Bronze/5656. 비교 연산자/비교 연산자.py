import sys

cnt = 0
while True:
    A, operator, B = sys.stdin.readline().split()
    A, B = int(A), int(B)
    cnt += 1

    result = True
    if operator == "E":
        break
    
    elif operator == ">":
        result = A > B
    elif operator == ">=":
        result = A >= B
    elif operator == "<":
        result = A < B
    elif operator == "<=":
        result = A <= B
    elif operator == "==":
        result = A == B
    else:
        result = A != B
    
    output = 'true' if result else 'false'

    print(f"Case {cnt}: {output}")