import sys
input = sys.stdin.readline

A, B = [input().rstrip() for _ in range(2)]
N, M = len(A), len(B)
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = (max(dp[i][j+1], dp[i+1][j]), dp[i][j]+1)[A[i]==B[j]]

print(dp[N][M])
