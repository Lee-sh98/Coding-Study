import sys
MOD = 9901

N = int(sys.stdin.readline())
a, b = 1, 1

for _ in range(N):
    a, b = (a+2*b)%MOD, (a+b)%MOD

print(a)
