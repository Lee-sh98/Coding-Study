import sys

dp = {0:1, 1:1}
for i in range(2, 251):
    dp[i] = dp[i-1]+2*dp[i-2]

while True:
    try:
        n = int(sys.stdin.readline())
        print(dp[n])
    except:
        break
