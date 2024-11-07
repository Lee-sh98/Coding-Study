import sys
input = sys.stdin.readline

M = int(input())
xor = 0
s = 0
for _ in range(M):
    c, *x = map(int, input().split())
    if c == 1:
        d = x[0]
        xor ^= d
        s += d
    elif c == 2:
        p = x[0]
        xor ^= p
        s -= p
    elif c == 3:
        print(s)
    else:
        print(xor)
