import sys

n = int(sys.stdin.readline())
q, r = divmod(n, 5)

while q>0 and r%2:
    q -= 1
    r += 5
r//=2

if q*5 + r*2 == n:
    print(q+r)
else:
    print(-1)
