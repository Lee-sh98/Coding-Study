import sys
input = sys.stdin.readline
INF = -int(1e9)

n = int(input())
dp = [INF]*2
result = INF

for m in map(int, input().split()):
    dp = [max(dp[0]+m, m), max(dp[1]+m, dp[0])]
    result = max(result, *dp)

print(result)
