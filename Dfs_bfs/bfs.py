from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue: # 큐가 빌 때까지 반복
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]] # 각 노드가 연결된 정보를 인접리스트로 표현

visited = [False] * 9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현

bfs(graph, 1, visited)
