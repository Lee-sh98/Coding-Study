import sys
from heapq import *
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    M, V = map(int, input().split())
    heappush(jewels, (M, V))

bags = [int(input()) for _ in range(K)]
bags.sort()

result = 0
tmp = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        _, value = heappop(jewels)
        heappush(tmp, -value)
    if tmp:
        result -= heappop(tmp)
    elif not jewels:
        break

print(result)
