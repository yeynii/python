N, M = map(int, input().split())
cnt = 0

while N != 1 :
  if N % M == 0:
    cnt += 1
    N /= M
  else:
    cnt += N % M
    N -= N % M

print(cnt)
