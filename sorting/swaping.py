n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse = True)

count = 0

for i in range(k):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
    count += 1
  else:
    break

print(sum(A))
