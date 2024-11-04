import sys
input = sys.stdin.readline
INF = -int(1e9)

n = int(input())
dp = [[INF]*3 for _ in range(n+1)]

dp = [[INF]*(n+1) for _ in range(3)]
dp[0] = list(map(int, input().split()))+[0]

for i in range(n):
    for j in [1, 2]:
        dp[j][i+1] = max(dp[j][i]+dp[0][i], dp[j-1][i])

print(max(map(max, dp[1:])))
