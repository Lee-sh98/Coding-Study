import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = int(graph[i][j] or (graph[i][k] and graph[k][j]))

for g in graph:
    print(" ".join(map(str, g)))
