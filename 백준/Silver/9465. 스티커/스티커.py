import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    sticker = list(map(list, zip(*(map(int, input().split()) for _ in range(2)))))
    
    dp = [[0, 0] for _ in range(n+2)]

    for i in range(n):
        for j in range(2):
            dp[i+2][j] = max(dp[i+1][j-1], dp[i][j-1]) + sticker[i][j]
    return max(dp[-1])


T = int(input())

for _ in range(T):
    result = solution()
    print(result)
    
