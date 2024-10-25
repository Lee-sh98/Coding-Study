import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [INF]*(k+1)
dp[0] = 0

for i in range(1, k+1):
    dp[i] = min(dp[i], min((dp[i-coin] for coin in coins if coin<=i), default=INF)+1)

print((dp[k], -1)[dp[k]==INF])
