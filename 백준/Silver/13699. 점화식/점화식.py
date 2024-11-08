import sys

n = int(sys.stdin.readline())
dp = dict.fromkeys(range(n+1), 0)
dp[0] = 1
for i in range(1, n+1):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]
    
print(dp[n])
