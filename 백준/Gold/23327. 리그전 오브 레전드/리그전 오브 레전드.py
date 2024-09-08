import sys
from itertools import combinations
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]*(N+1)
tp = [0]*(N+1)

for i in range(N):
    dp[i+1] = dp[i] + arr[i]
    tp[i+1] = tp[i] + dp[i]*arr[i]

for _ in range(Q):
    l, r = map(int, input().split())

    ans = tp[r]-tp[l-1]-(dp[r]-dp[l-1])*dp[l-1]
    print(ans)
