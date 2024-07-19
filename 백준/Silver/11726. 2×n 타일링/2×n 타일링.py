# 11726 2*n tiling

import sys

n = int(sys.stdin.readline())

dp = list(range(n+1))

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

sys.stdout.write(str(dp[n]%10007)+"\n")
