location = input()

x = ord(location[0]) - ord('a') + 1
y = int(location[1]) 

steps = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
count = 0

for s in steps:
  if x + s[0] in range(1, 8) and y + s[1] in range(1,8):
    count += 1

print(count)
