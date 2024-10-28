import sys
from heapq import *
input = lambda: list(map(int, sys.stdin.readline().split()))
INF = int(1e9)

L, N, K = input()
lights = input()
street = {}

for l in lights:
    street[l] = 0

q = [(0, l) for l in lights]
while q and len(street) < K:
    brightness, cur = heappop(q)
    if street.get(cur, INF) < brightness:
        continue
    for d in [-1, 1]:
        node = cur+d
        if 0<=node<=L and brightness+1 < street.get(node, INF):
            street[node] = brightness+1
            heappush(q, (brightness+1, node))
print("\n".join(map(str, sorted(street.values())[:K])))
