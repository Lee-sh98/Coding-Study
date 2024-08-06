import sys

def fib_recursion(n):
    global cnt_recursion
    if n==1 or n==2:
        return 1
    else:
        cnt_recursion += 1
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib_dp(n):
    global cnt_dp
    
    dp = {1:1, 2:1}
    for i in range(3, n+1):
        cnt_dp += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


cnt_recursion, cnt_dp = 1, 0
n = int(sys.stdin.readline())

fib_recursion(n)
fib_dp(n)

print(cnt_recursion, cnt_dp)
