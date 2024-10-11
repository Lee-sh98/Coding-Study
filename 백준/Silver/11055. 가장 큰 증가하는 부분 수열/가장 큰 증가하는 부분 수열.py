import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [a for a in arr]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))
