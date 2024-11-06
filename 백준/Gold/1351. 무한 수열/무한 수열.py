import sys

def solve(x):
    if x< 0:
        return 0

    if x not in dp:
        dp[x] = solve(int(x/P))+solve(int(x/Q))

    return dp[x]

N, P, Q = map(int, sys.stdin.readline().split())
dp = {0:1}

print(solve(N))
