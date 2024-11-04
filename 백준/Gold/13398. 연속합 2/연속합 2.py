import sys
input = sys.stdin.readline
INF = -int(1e9)

n = int(input())
arr = list(map(int, input().split()))
dp = [[INF]*2 for _ in range(n+1)]

for i in range(n):
    dp[i+1][0] = max(dp[i][0], 0)+arr[i]
    dp[i+1][1] = max(dp[i][1]+arr[i], dp[i][0])

print(max(map(max, dp[1:])))
