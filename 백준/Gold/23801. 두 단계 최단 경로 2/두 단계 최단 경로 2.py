import sys
from heapq import *
input = sys.stdin.readline
INF = 2 * 1000000 * 100000 + 1

def dijkstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0

    q = [(0, start)]
    while q:
        dist, cur = heappop(q)

        if distance[cur] < dist:
            continue
        for node, ndist in edges[cur]:
            cost = dist + ndist
            if cost < distance[node]:
                distance[node] = cost
                heappush(q, (cost, node))

    return distance

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

X, Z = map(int, input().split())
P = int(input())
PS = list(map(int, input().split()))

DX, DZ = map(dijkstra, [X, Z])

MIN = INF
for p in PS:
    if DX[p] == INF or DZ[p] == INF:
        continue
    cur = DX[p]+DZ[p]
    if cur < MIN:
        MIN = cur

if MIN == INF:
    print(-1)
else:
    print(MIN)
