n, m = map(int, input().split())

result = 1

for i in range(n):
  cardset = list(map(int, input().split()))
  if result < min(cardset):
    result = min(cardset)

print(result)
