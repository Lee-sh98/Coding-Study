import sys
from collections import deque
from heapq import *
input = lambda: map(int, sys.stdin.readline().split())

L, N, K = input()
lights = list(input())
street = [L]*(L+1)

q = [(0, light) for light in lights]
for l in lights:
    street[l] = 0

while q:
    brightness, cur = heappop(q)
    if street[cur] < brightness:
        continue
    for d in [-1, 1]:
        node = cur+d
        if 0<=node<=L and brightness+1 < street[node]:
            street[node] = brightness+1
            heappush(q, (brightness+1, node))

print("\n".join(map(str, sorted(street)[:K])))
