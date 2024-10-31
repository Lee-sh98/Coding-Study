import sys
input = sys.stdin.readline

k = 1
while (N:=int(input())):
    dp = [list(map(int, input().split())) for _ in range(N)]
    dp[0][0] = 1_000_000
    dp[0][2] += dp[0][1]
    
    for i in range(1, N):
        for j in range(3):
            if j==0:
                dp[i][j] += min(dp[i-1][:2])
            else:
                dp[i][j] += min(dp[i][j-1], *dp[i-1][j-1:])
    print(f"{k}. {dp[N-1][1]}")
    k += 1
