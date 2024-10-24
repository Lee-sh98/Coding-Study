import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*3
tmp = [0]*3
for c in cost:
    for i in range(3):
        tmp[i] = c[i] + min(dp[:i]+dp[i+1:])
    dp = tmp[:]

print(min(dp))
