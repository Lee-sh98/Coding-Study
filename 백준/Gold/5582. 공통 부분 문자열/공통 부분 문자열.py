import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
N, M = len(A), len(B)

dp = [[0]*(M+1) for _ in range(N+1)]
result = 0
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            result = max(result, dp[i+1][j+1])

print(result)
