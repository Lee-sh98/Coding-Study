import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
graph = [list(input()) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i==0:
            dp[i][j] = dp[i][j-1]
        elif j==0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        dp[i][j] += graph[i][j]

print(dp[N-1][M-1])
