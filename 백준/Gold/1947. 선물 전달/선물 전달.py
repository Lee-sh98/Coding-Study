import sys
MOD = 1_000_000_000
N = int(sys.stdin.readline())
dp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = (dp[i-1]*i + (1, -1)[i%2])%MOD
print(dp[N])
