import sys

N, r, c = map(int, sys.stdin.readline().split())

x, y = 2**(N-1), 2**(N-1)
count = 0

while x>0:
    if r>=x:
        count += 2*(x**2)
        r -= x
    x//=2

while y>0:  
    if c>=y:
        count += y**2
        c -= y
    y //= 2

print(count)
