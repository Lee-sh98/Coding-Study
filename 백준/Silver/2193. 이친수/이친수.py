import sys

def solution(N):
    dp = [1, 0] # dp[i] means the numer of pinary number ending with 'i'
    for _ in range(N-2):
        dp[0], dp[1] = dp[0]+dp[1], dp[0]
    return sum(dp)

N = int(sys.stdin.readline())
print(solution(N))
