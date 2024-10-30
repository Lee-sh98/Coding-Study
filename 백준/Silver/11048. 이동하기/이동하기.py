import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
graph = [[0]*(M+1)]+[[0]+list(input()) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        graph[i][j] += max(graph[i][j-1], graph[i-1][j])
print(graph[N][M])
