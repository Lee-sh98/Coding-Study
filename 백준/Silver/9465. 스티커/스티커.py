import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    sticker = list(list(map(int, input().split())) for _ in range(2))
    dp = [[0]*(n+2) for _ in range(2)]

    for i in range(n):
        for j in range(2):
            dp[j][i+2] = max(dp[j-1][i+1], dp[j-1][i]) + sticker[j][i]
    return max(dp[0][-1], dp[1][-1])


T = int(input())

for _ in range(T):
    result = solution()
    print(result)
    
