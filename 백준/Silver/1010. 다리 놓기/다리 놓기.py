T = int(input())

def combination(N, M):
  if N == M:
    return 1
  
  output = 1
  divide = 1
  for i in range(M, M-N, -1):
    output *= i
  for i in range(1, N+1):
      divide *= i
  return output // divide

for _ in range(T):
  N, M = map(int, input().split(' '))
  print(combination(N, M))