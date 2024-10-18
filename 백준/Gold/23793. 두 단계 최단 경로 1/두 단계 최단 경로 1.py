import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(graph, start, end):
    distance = [INF]*(N+1)
    distance[start] = 0

    q = [(0, start)]
    while q:
        dist, cur = heappop(q)
        if distance[cur] < dist:
            continue
        for node, ndist in graph[cur]:
            cost = dist+ndist

            if cost < distance[node]:
                distance[node] = cost
                heappush(q, (cost, node))

    if distance[end] != INF:
        return distance[end]
    else:
        return -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
x, y, z = map(int, input().split())
without_Y = [[] for _ in range(N+1)]
merged = [[] for _ in range(N+1)]

for u, v, w in arr:
    if not(u == y or v == y):
        without_Y[u].append((v, w))
    merged[u].append((v, w))

to_Y, to_Z = dijkstra(merged, x, y), dijkstra(merged, y, z)
r1 = to_Y+to_Z if to_Y != -1 and to_Z != -1 else -1
r2 = dijkstra(without_Y, x, z)

print(r1, r2)
