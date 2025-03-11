import sys 

input = sys.stdin.readline
A, B = map(int, input().split())

cnt = 1
while A < B:
    cnt += 1
    if B % 10 == 1:
        B = B // 10
        
    elif B % 2 == 0:
        B = B // 2

    else:
        flag = True
        print(-1)
        exit()
    
if A == B:
    print(cnt)
else:
    print(-1)