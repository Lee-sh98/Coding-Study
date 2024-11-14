import sys
input = sys.stdin.readline

N, M = map(int,input().split())
chapters = [[*map(int, input().split())] for _ in range(M)]
dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        day, page = chapters[i-1]
        if j < day:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day]+page)

print(dp[M][N])
