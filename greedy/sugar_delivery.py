N = int(input())

x = N // 5
result = -1

while x >= 0 :
  if (N - 5 * x) % 3 == 0 :
    y = (N - 5 * x) / 3
    result = int(x + y)
    break
  x -= 1

print(result)
