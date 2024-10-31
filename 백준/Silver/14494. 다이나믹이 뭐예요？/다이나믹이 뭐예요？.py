import sys
MOD = 1_000_000_007

n, m = map(int, sys.stdin.readline().split())
dp = [[0]*(m) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i==0 or j==0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]+dp[i-1][j-1])%MOD

print(dp[n-1][m-1])
