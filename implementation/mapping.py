N, M = map(int, input().split()) # 맵 크기
A, B, d = map(int, input().split()) # A: col B: row, 방향
maps = [list(map(int, input().split())) for _ in range(N)] # 맵 타입 입력 1:바다, 0:육지, -1:갔던 곳
direction = [[-1, 0] , [0, 1], [1, 0], [0, -1]] # 북, 동, 남, 서
count = 1

while True:
  maps[B][A] = -1
  if maps[B+1][A] != 0 and maps[B-1][A] != 0 and maps[B][A+1] != 0 and maps[B][A-1] != 0: #사방이 바다or갔던곳
    if d == 0 or d == 1:
      if maps[B + direction[d+2][0]][A + direction[d+2][1]] == 1: # 뒤가 바다
        break
      else: # 왔던길 돌아가기
        A += direction[d+2][1]
        B += direction[d+2][0]
        continue
    elif d == 2 or d == 3: 
      if maps[B + direction[d-2][0]][A + direction[d-2][1]] == 1: # 뒤가 바다
        break
      else: # 왔던길 돌아가기
        A += direction[d-2][1]
        B += direction[d-2][0]
        continue

  if d == 0:
    d = 3
  else:
    d -= 1

  if maps[B + direction[d][0]][A + direction[d][1]] == 0:
    A += direction[d][1]
    B += direction[d][0]
    count += 1

print(count)
