import sys
input = sys.stdin.readline

def solution(arr):
    n = len(arr)
    if n<3:
        return sum(arr)

    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = dp[0] + arr[1]
    dp[2] = max(arr[0]+arr[1], arr[1]+arr[2], arr[0]+arr[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])

    return dp[-1]

n = int(input())
arr = list(int(input()) for _ in range(n))

result = solution(arr)
print(result)
