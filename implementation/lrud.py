N = int(input())
plan = input().split()

x, y = 1, 1

for p in plan:
  if p == 'L':
    if y > 1:
      y -= 1
  elif p == 'R':
    if y < N:
      y += 1
  elif p == 'U':
    if x > 1:
      x -= 1
  elif p == 'D':
    if x < N:
      x += 1

print(x, y)
