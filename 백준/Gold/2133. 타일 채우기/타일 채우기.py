import sys

N = int(sys.stdin.readline())
dp = [0]*(N+1)
dp[0] = 1

for i in range(2, N+1, 2):
    dp[i] = dp[i-2] + sum(dp[:i])*2
print(dp[N])
