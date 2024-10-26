import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
A = list(map(int, input().split()))
dp = [INF]*N
dp[0] = 0

for i in range(N):
    for j in range(i+1, min(i+A[i]+1, N)):
        dp[j] = min(dp[j], dp[i]+1)

print((dp[N-1], -1)[dp[N-1]==INF])
