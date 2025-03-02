N = int(input())

queens = [0] * N
result = 0

def put_a_queen(row):
    global result
    if row == N:
        result += 1
        return
    
    for col in range(N):
        queens[row] = col
        if check(row):
            put_a_queen(row+1)


def check(row):
    
    for before_row in range(row):
        if queens[before_row] == queens[row] or abs(queens[before_row] - queens[row]) == abs(before_row - row):
            return False
    
    return True

put_a_queen(0)
print(result)