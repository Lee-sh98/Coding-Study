import sys
input = sys.stdin.readline

def equal(i, j):
    return arr[i] == arr[j]

N = int(input())
A = list(map(int, input().split()))
B = A[::-1]
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(N-dp[N][N])
