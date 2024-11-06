import sys
MOD = 1_000_000_000

n = int(sys.stdin.readline())
a, b = 0, 1
for i in range(abs(n)):
    a, b = b, (a+b)%MOD

if n<0 and not n%2:
    print(-1)
elif abs(n)>0:
    print(1)
else:
    print(0)
print(abs(a))
