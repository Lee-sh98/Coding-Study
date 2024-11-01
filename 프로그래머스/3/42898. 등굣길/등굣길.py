def solution(m, n, puddles):
    MOD = 1_000_000_007
    arr = [[0]*(m+1) for _ in range(n+1)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for x, y in puddles:
        arr[y][x] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j]:
                continue
            dp[i][j] += (dp[i-1][j] + dp[i][j-1])%MOD
    return dp[n][m]