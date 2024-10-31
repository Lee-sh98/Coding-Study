import sys
input = lambda:int(sys.stdin.readline())

dp = [[0]*11 for _ in range(66)]
dp[1] = [1]*11
for i in range(2, 66):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

T = input()
for _ in range(T):
    print(dp[input()+1][-1])
