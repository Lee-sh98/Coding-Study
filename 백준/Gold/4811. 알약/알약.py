import sys
input = sys.stdin.readline

dp = [0]*31
dp[0] = 1
for i in range(1, 31):
    dp[i] = sum(dp[j]*dp[i-j-1]for j in range(i))

while (N:=int(input())):
    print(dp[N])
