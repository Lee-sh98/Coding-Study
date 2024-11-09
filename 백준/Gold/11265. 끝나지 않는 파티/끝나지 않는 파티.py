import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for _ in range(M):
    A, B, C = map(int, input().split())
    print(("Enjoy other party", "Stay here")[dp[A-1][B-1]>C])
