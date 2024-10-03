import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _  in range(N)]
dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    time, pay = schedule[i]
    if i+time>N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+time]+pay)

print(dp[0])
