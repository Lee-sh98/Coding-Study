import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i==0 or j==0 or not dp[i][j]:
            continue
        dp[i][j]+=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        
result = max(map(max, dp))
print(result*result)
