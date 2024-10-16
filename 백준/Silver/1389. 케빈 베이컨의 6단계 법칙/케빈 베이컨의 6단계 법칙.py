import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF]*N for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A-=1; B-=1
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(N):
    graph[k][k] = 0
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

print(sorted(range(N), key=lambda x: (sum(graph[x]),x))[0]+1)
