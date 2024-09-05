import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
q = []
result = 0

for _ in range(N):
    heappush(q, int(input()))

while len(q)>1:
    s = heappop(q) + heappop(q)
    result += s
    heappush(q, s)
print(result)
