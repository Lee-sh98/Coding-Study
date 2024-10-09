import sys
input = sys.stdin.readline
INF = int(1e10)

N, M, T = map(int, input().split())
graph = [[INF]*N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    u, v, h = map(int, input().split())
    graph[u-1][v-1] = h

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], max(graph[i][k], graph[k][j]))

for _ in range(T):
    s, e = map(int, input().split())

    if graph[s-1][e-1] != INF:
        print(graph[s-1][e-1])
    else:
        print(-1)
