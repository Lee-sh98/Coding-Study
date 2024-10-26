import sys

L, R = sys.stdin.readline().split()
c = 0
if len(L) == len(R):
    for l, r in zip(L, R):
        if l!=r:
            break
        if l==r=='8':
            c += 1

print(c)
