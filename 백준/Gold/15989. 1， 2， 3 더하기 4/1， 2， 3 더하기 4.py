import sys
MAX = 10_001

input = lambda:int(sys.stdin.readline())

dp = [[0]*3 for _ in range(MAX)]
dp[1] = [1,0,0]
dp[2] = [1,1,0]
dp[3] = [1,1,1]
for i in range(4, MAX):
    for j in [1,2,3]:
        dp[i][j-1] = sum(dp[i-j][:j])
n = input()
for _ in range(n):
    print(sum(dp[input()]))
