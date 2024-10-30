import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
graph = [list(input()) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])+graph[i-1][j-1]
print(dp[N][M])
