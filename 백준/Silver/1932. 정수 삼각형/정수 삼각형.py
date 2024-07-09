import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*n
tmp = [0]*n

for _ in range(n):
    line = list(map(int, input().split()))
    for i in range(l:=len(line)):
        tmp[i] = line[i] + max(dp[max(0, i-1): i+1])

    for j in range(l):
        dp[j] = tmp[j]

print(max(dp))
