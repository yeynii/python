N, M = map(int, input().split())

cnt = 0

while N != 1 :
  if N % M == 0:
    N /= M
  else:
    N -= 1
  cnt += 1

print(cnt)
