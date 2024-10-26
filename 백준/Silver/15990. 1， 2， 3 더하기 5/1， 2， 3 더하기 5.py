import sys
input = sys.stdin.readline
MOD = 1_000_000_009
        
T = int(input())
r = [1, 2, 3]
nums = [int(input()) for _ in range(T)]
MAX = max(nums)+1

dp = [[0, 0, 0] for _ in range(MAX)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, MAX):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%MOD
    dp[i][1] = (dp[i-2][0] + dp[i-2][2])%MOD
    dp[i][2] = (dp[i-3][0] + dp[i-3][1])%MOD
    
for num in nums:
    print(sum(dp[num])%MOD)
