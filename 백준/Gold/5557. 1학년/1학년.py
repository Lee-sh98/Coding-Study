import sys
input = sys.stdin.readline

N = int(input())
*arr, target = map(int, input().split())
dp = [0]*21
dp[arr[0]] = 1

for a in arr[1:]:
    tmp = [0]*21
    for j in range(21):
        tmp[j] += sum(dp[k] for k in [j+a, j-a] if 0<=k<=20)
    dp = tmp[:]

print(dp[target])
