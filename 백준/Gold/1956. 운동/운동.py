import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
visited = [0]*(V+1)
indegree = [0]*(V+1)
outdegree = [0]*(V+1)
graph = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    outdegree[a] = 1
    indegree[b] = 1

for k in range(1, V+1):
    if not (indegree[k] and outdegree[k]):
        continue
    for i in range(1, V+1):
        if graph[i][k] == INF:
            continue
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

MIN = INF
for i in range(1, V+1):
    MIN = min(MIN, graph[i][i])

print((-1, MIN)[MIN!=INF])
