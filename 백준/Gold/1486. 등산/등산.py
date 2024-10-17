import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e8)
A = ord('A')
a = ord('a')

def input_line():
    result = []
    for c in map(ord,input().rstrip()):
        if A <= c <= A+25:
            result.append(c - A)
        else:
            result.append(c - a + 26)
    return result

N, M, T, D = map(int, input().split())
graph = [input_line() for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

dp = [[[[INF]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for x in range(N):
    for y in range(M):
        dp[x][y][x][y] = 0
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<M):
                continue
            dh = graph[x][y] - graph[nx][ny]
            if abs(dh) > T:
                continue
            dp[x][y][nx][ny] = min(dp[x][y][nx][ny], 1 if dh >= 0 else dh**2)

for i in range(N):
    for j in range(M):
        for u in range(N):
            for v in range(M):
                for x in range(N):
                    for y in range(M):
                        dp[u][v][x][y] = min(dp[u][v][x][y], dp[u][v][i][j]+dp[i][j][x][y])
MAX = 0
for x in range(N):
    for y in range(M):
        cost = dp[0][0][x][y] + dp[x][y][0][0]
        if cost < INF and cost <= D:
            MAX = max(MAX, graph[x][y])

print(MAX)
