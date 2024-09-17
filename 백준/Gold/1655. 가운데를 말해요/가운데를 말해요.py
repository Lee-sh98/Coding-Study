import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
lq, rq = [], [] # max heap and min heap

for _ in range(N):
    num = int(input())

    if len(lq) == len(rq):
        heappush(lq, -num)
    else:
        heappush(rq, num)

    if rq and -lq[0]>rq[0]:
        lv = -heappop(lq)
        rv = -heappop(rq)

        heappush(lq, rv)
        heappush(rq, lv)

    print(-lq[0])
