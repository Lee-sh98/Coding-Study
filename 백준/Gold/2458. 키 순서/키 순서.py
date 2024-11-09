import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
dp = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    dp[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

tp = list(map(list, zip(*dp)))

result = 0
for i in range(N):
    result += sum(dp[i])+sum(tp[i]) == N-1
print(result)
