import sys
from math import sqrt

n = int(sys.stdin.readline())
dp = [4]*(n+1)

for i in range(1, int(sqrt(n))+1):
    dp[i*i] = 1

for i in range(1, n+1):
    if dp[i] == 1:
        continue

    j = 1
    while j*j<=i:
        dp[i] = min(dp[i], 1+dp[i-j*j])
        j+=1

print(dp[n])
