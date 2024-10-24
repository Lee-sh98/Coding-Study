import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
K = int(input())
graph = [[0]*21 for _ in range(N+1)]
graph[0][1] = 1

dp = [[INF]*21 for _ in range(N+1)]
dp[0][1] = 0

for i in range(1, N+1):
    M, *holes = map(int, input().split())
    for hole in holes:
        graph[i][hole] = 1

for i in range(N):
    for j in range(1, 21):
        if not graph[i][j]:
            continue

        for k in [j, j+1, min(2*j, 20), j-1]:
            if 1<=k<21 and graph[i+1][k]:
                dp[i+1][k] = min(dp[i+1][k], dp[i][j])

        for k in range(1, 21):
            if graph[i+1][k]:
                dp[i+1][k] = min(dp[i+1][k], dp[i][j]+1)

result = INF
for d in dp[N][1:]:
    if d > K:
        continue
    result = min(result, d)
print((result, -1)[result>=INF])
