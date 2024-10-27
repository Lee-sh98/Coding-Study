import sys

def solve(x, y):
    if x<y:
        return 0
    if x==y or y==0:
        return 1
    if (x, y) not in dp:
        dp[x, y] = solve(x-1, y-1) + solve(x-1, y)

    return dp[x, y]

n, k = map(int, sys.stdin.readline().split())
dp = {}

print(solve(n-1, k-1))
