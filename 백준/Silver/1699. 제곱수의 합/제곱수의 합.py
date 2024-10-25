import sys
from math import sqrt

N = int(sys.stdin.readline())
sq = []
dp = [0]*(N+1)

for i in range(1, N+1):
    if sqrt(i)%1 == 0:
        sq.append(i)
    dp[i] = min(dp[i-s] for s in sq)+1

print(dp[N])
