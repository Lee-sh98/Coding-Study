import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    idx = dict(zip(coins, range(N)))
    
    dp = [[0]*N for _ in range(M+1)]

    for coin in coins:
        dp[coin][idx[coin]] = 1
        
    for cur in range(1, M+1):
        for coin in coins:
            if cur>=coin:
                dp[cur][idx[coin]] += sum(dp[cur-coin][:idx[coin]+1])
    
    print(sum(dp[M]))
