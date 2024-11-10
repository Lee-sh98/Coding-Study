import sys

def solve(n):
    global MAX
    if n not in dp:
        for i in range(MAX, n+1):
            dp[i] = dp[i-1]+2*dp[i-2]
        MAX = n+1
    return dp[n]

dp = {0:1, 1:1}
MAX = 2
while True:
    try:
        n = int(sys.stdin.readline())
        print(solve(n))
    except:
        break
