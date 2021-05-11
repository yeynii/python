N = int(input())

meeting_time = [[0 for i in range(2)] for j in range(N)]

for i in range(N):
    meeting_time[i] = list(map(int, input().split()))

meeting_time.sort(key=lambda x : (x[1], x[0]))

end = meeting_time[0][1]
result = 1

for i in range(1,N):
    if end <= meeting_time[i][0]:
      end = meeting_time[i][1]
      result += 1

print(result)
