import sys
from heapq import *
input = lambda: int(sys.stdin.readline())

N = input()
hq = []
heapify(hq)

for _ in range(N):
    x = input()

    if not x:
        if hq:
            print(heappop(hq)[1])
        else:
            print(0)
    else:
        heappush(hq, (abs(x), x))
