import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dp = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a==b==-1:
        break
    dp[b][a] = dp[a][b] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

score, president = INF, []
for i in range(1, n+1):
    MAX = max(dp[i][1:])
    if score > MAX:
        score = MAX
        president = [i]
    elif score == MAX:
        president.append(i)

print(score, len(president))
print(" ".join(map(str, president)))
