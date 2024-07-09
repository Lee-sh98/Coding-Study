import sys
from heapq import *
input = sys.stdin.readline

def dp():
    mem = []
    heapify(mem)

    def helper(n):
        if n==0:
            if mem:
                print(heappop(mem))
            else:
                print(0)
        else:
            heappush(mem, n)
    return helper

action = dp()
N = int(input())
for _ in range(N):
    action(int(input()))
