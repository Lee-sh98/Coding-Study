import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    for n in map(int, input().split()):
        heappush(q, n)
    while len(q) > N:
        heappop(q)

print(q[0])
