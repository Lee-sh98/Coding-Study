import sys
input = sys.stdin.readline

def calc(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x1][y2] - dp[x2][y1] + dp[x1][y1]

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = arr[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j]

result = 0

for i in range(N):
    top = calc(0, 0, i, M)
    for j in range(i, N):
        mid = calc(i, 0, j, M)
        bottom = calc(j, 0, N, M)
        tmp = top*mid*bottom
        result = max(result, tmp)

for i in range(M):
    left = calc(0, 0, N, i)
    for j in range(i, M):
        mid = calc(0, i, N, j)
        right = calc(0, j, N, M)
        tmp = left*mid*right
        result = max(result, tmp)

for i in range(N):
    top = calc(0, 0, i, M)
    for j in range(M):
        left = calc(i, 0, N, j)
        right = calc(i, j, N, M)
        tmp = top*left*right
        result = max(result, tmp)

    bottom = calc(i, 0, N, M)
    for j in range(M):
        left = calc(0, 0, i, j)
        right = calc(0, j, i, M)
        tmp = bottom*left*right
        result = max(result, tmp)

for j in range(M):
    left = calc(0, 0, N, j)
    for i in range(N):
        top = calc(0, j, i, M)
        bottom = calc(i, j, N, M)
        tmp = left*top*bottom
        result = max(result, tmp)
    right = calc(0, j, N, M)
    for i in range(N):
        top = calc(0, 0, i, j)
        bottom = calc(i, 0, N, j)
        tmp = right*top*bottom
        result = max(result, tmp)

print(result)
