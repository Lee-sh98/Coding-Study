import sys
MAX = 1_000_001
MOD = 1_000_000_009
input = lambda:int(sys.stdin.readline())

dp = [0]*MAX
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, MAX):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%MOD
N = input()
for _ in range(N):
    print(dp[input()])
