import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [-1e9]*n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1], 0) + arr[i]

print(max(dp))
