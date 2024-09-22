import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j==0:
            continue
        c1, c2 = INF, INF
        if j!=0:
            c1 = dp[i][j-1] + max(0, arr[i][j]-arr[i][j-1]+1)
        if i!=0:
            c2 = dp[i-1][j] + max(0, arr[i][j]-arr[i-1][j]+1)

        dp[i][j] = min(c1, c2)

print(dp[n-1][n-1])
