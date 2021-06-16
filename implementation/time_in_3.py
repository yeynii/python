N = int(input())

count = 0

for h in range(N+1):
  if h in [3, 13, 23]:
    count += 60 * 60
    continue
  for m in range(60):
    if m//10 == 3 or m%10 == 3:
      count += 60
      continue
    for s in range(60):
      if (s//10 == 3) or (s%10 == 3):
        count += 1
print(count)
