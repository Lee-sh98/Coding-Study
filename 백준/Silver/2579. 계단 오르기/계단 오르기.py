# 2579 ascending stairs
import sys
input = sys.stdin.readline

def ascend(point):
    dp = [0]*(n+1)
    dp[1] = point[1]
    dp[2] = dp[1] + point[2]


    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

    return dp[-1]


n = int(input())
point = [0]+[int(input()) for i in range(n)]

if n<3:
    print(sum(point))
else:
    print(ascend(point))
