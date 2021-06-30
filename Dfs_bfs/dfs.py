def dfs(graph, v, visited): # DFS 메서드 정의
	visited[v] = True # 현재 노드를 방문처리
	print(v, end=' ')

	for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
		if not visited[i]:
			dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]] # 각 노드가 연결된 정보를 인접리스트로 표현

visited = [False] * 9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현

dfs(graph, 1, visited)
