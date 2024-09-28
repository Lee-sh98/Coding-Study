import sys

def supply1(prev, cover):
    for p in prev:
        yield p.join(cover)

def supply2(prev):
    for p in zip(prev, prev):
        yield " ".join(p)

def solve(n):
    if n==3:
        return ["  *  ", " * * ", "*****"]

    n >>= 1
    prev = solve(n)
    result = []
    cover = [" "*n, " "*n]
    
    r1 = list(supply1(prev, cover))
    r2 = list(supply2(prev))
    
    return r1+r2

N = int(sys.stdin.readline())
result = solve(N)
for r in result:
    print(r)
