n, m = map(int, input().split())

result = 0

for i in range(n):
    cards = list(map(int, input().split()))
    result = max(result, min(cards))

print(result)
