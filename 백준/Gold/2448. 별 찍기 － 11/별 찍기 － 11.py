import sys

def supply1(prev, n):
    cover = [" "*n, " "*n]
    for p in prev:
        yield p.join(cover)

def supply2(prev):
    yield from map(" ".join, zip(prev, prev))

def solve(n):
    if n==3:
        return ["  *  ", " * * ", "*****"]

    n //= 2
    prev = solve(n)
    
    r1 = list(supply1(prev, n))
    r2 = list(supply2(prev))
    
    return r1+r2

N = int(sys.stdin.readline())
result = solve(N)
for r in result:
    print(r)
