import sys

def solve(x):
    if x not in dp:
        p,q=divmod(x,2)
        dp[x]=p*(p+q)+solve(p)+solve(p+q)
    return dp[x]
N=int(sys.stdin.readline())
dp={0:0,1:0}
print(solve(N))
