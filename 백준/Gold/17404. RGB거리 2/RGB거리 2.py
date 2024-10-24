import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
cost = [tuple(map(int, input().split())) for _ in range(N)]

answer = INF
color = [0, 1, 2]
tmp = [0]*3

for c in color:
    dp = [INF, INF, INF]
    dp[c] = cost[0][c]
    
    for i in range(1, N):
        for d in color:
            tmp[d] = min(dp[:d]+dp[d+1:]) + cost[i][d]
        dp = tmp[:]
    dp[c] = INF
    answer = min(answer, *dp)

print(answer)
