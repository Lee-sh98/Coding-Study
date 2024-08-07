import sys
from math import log2
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [int(input()) for _ in range(Q)]
town = [0]*(N+1)

for q in arr:
    cur = q
    mem = -1
    while cur != 1:
        if town[cur]:
            mem = cur
        cur //= 2

    if mem != -1:
        print(mem)
    else:
        print(0)
    town[q] = 1
