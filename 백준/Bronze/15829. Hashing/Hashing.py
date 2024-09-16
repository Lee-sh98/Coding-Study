import sys
input = sys.stdin.readline

r = 31
M = 1234567891
def hashing(lst, r, m):
    ri = 1
    H = 0
    for a in lst:
        H += a*ri
        ri *= r
        H %= m
    return H

L = int(input())
S = input().rstrip()
mapper = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1, 27)))
lst = list(map(mapper.__getitem__, S))

print(hashing(lst, r, M))
