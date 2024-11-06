import sys
input = sys.stdin.readline

N = int(input())
*arr, target = list(map(int, input().split()))
dp = [[0]*21 for _ in range(N-1)]
dp[0][arr[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        for k in [arr[i], -arr[i]]:
            if 0<=j+k<=20:
                dp[i][j]+=dp[i-1][j+k]

print(dp[N-2][target])
