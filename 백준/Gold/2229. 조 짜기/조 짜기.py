import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    for j in range(i):
        cur = arr[j:i+1]
        dp[i] = max(dp[i], dp[j-1]+abs(max(cur)-min(cur)))

print(dp[N-1])
