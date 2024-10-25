import sys
N = int(sys.stdin.readline())

sq = []
dp = list(range(N+1))

i = 1
while i*i <= N:
    sq.append(i*i)
    i += 1

for s in sq:
    for i in range(s, N+1):
        dp[i] = min(dp[i], dp[i-s]+1)

print(dp[N])
