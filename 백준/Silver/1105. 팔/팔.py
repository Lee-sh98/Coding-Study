import sys

L, R = input().split()

if len(L) != len(R):
    print(0)
else:
    c = 0
    for l, r in zip(L, R):
        if l!=r:
            break
        if l==r=='8':
            c += 1

    print(c)
