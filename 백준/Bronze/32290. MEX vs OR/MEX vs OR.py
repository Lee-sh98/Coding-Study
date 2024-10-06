import sys

def mex(a):
    return min(set(range(max(a)+2))-set(a))

l, r, x = map(int, sys.stdin.readline().split())
print(mex(list(map(x.__or__, range(l, r+1)))))
