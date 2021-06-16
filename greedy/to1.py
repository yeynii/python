N, K = map(int, input().split())

count = N % K
N -= N % K

while N >= K:
  if N % K == 0:
    N = N / K
    count += 1
  else:
    count += N % K
    N -= N % K

if N > 1:
  count += N-1

print(count)
