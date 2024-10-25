import sys
MOD = 1_000_000_000
                
N, K = map(int, sys.stdin.readline().split())
a = b = 1

for i in range(1, K):
    a *= N+i
    b *= i

print(a//b%MOD)
