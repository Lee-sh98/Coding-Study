import sys
input = sys.stdin.readline

N = int(input())

max_dp = [0]*3
min_dp = [0]*3

max_tmp = [0]*3
min_tmp = [0]*3

for _ in range(N):
    line = list(map(int, input().split()))
    
    for i in range(3):
        max_tmp[i] = line[i] + max(max_dp[max(i-1, 0): i+2])
        min_tmp[i] = line[i] + min(min_dp[max(i-1, 0):i+2])
        
    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]
    
print(max(max_dp), min(min_dp))
    
