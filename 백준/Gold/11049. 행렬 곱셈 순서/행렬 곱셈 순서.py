import sys
input = sys.stdin.readline

N = int(input())
m = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N) for _ in range(N)]

for t in range(1, N):
    for i in range(N-t):
        j = i+t
        if t==1:
            dp[i][j] = m[i][0]*m[j][0]*m[j][1]
            continue
        dp[i][j] = 2**32
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+m[i][0]*m[k][1]*m[j][1])

print(dp[0][N-1])
