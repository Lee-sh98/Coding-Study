import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
arr = list(map(int, input().split()))
dp = [INF]*(N+1)
dp[0] = 0

for cur in range(1, N+1):
    for card in range(N):
        if cur>=card:
            dp[cur] = min(dp[cur], dp[cur-card-1]+arr[card])

print(dp[N])
