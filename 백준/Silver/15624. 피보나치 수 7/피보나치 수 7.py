import sys
MOD = 1_000_000_007

n = int(sys.stdin.readline())
a, b = 0, 1

for i in range(n):
    a, b = b, (a+b)%MOD
print(a)
