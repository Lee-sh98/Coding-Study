import sys

N = int(sys.stdin.readline())
dp = [[1]*10 for _ in range(N)]

for i in range(1, N):
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[N-1])%10007)
