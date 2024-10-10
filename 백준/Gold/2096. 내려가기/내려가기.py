import sys
input = sys.stdin.readline

N = int(input())
M, m = [0]*3, [0]*3

for _ in range(N):
    tmp_M, tmp_m = [0]*3, [0]*3
    
    for i, c in enumerate(map(int, input().split())):
        tmp_M[i] = c + max(M[max(i-1, 0):i+2])
        tmp_m[i] = c + min(m[max(i-1, 0):i+2])
    M, m = tmp_M, tmp_m
    
print(max(M), min(m))
