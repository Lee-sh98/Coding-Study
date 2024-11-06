import sys
input = sys.stdin.readline

N = int(input())
*arr, target = map(int, input().split())
dp = [[0]*21 for _ in range(N-1)]
dp[0][arr[0]] = 1

for i, a in enumerate(arr[1:]):
    for j in range(21):
        for k in filter(lambda x: 0<=j+x<=20, [a, -a]):
            dp[i+1][j]+=dp[i][j+k]
        
print(dp[N-2][target])
