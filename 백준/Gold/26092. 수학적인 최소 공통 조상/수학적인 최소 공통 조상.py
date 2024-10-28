import sys

def factorize(x):
    factors = set([1, x])
    d = 2
    D = int(x**0.5)
    while x>1 and d <= D:
        if not x%d:
            x//=d
            factors.add(x)
        else:
            d += 1
    return factors

a, b = map(int, sys.stdin.readline().split())
aList = factorize(a)
bList = factorize(b)

print(max(aList&bList))
