import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distances = [INF]*(V+1)
    distances[start] = 0

    q = [(0, start)]
    while q:
        dist, cur = heappop(q)

        if distances[cur] < dist:
            continue

        for node, next_dist in edges[cur]:
            cost = dist + next_dist

            if cost < distances[node]:
                distances[node] = cost
                heappush(q, (cost, node))

    return [d if d != INF else -1 for d in distances]

N, V, E = map(int, input().split())
A, B = map(int, input().split())
H = list(map(int, input().split()))
edges = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, l = map(int, input().split())
    edges[a].append((b, l))
    edges[b].append((a, l))

D = list(map(int.__add__, dijkstra(A), dijkstra(B)))
print(sum(map(D.__getitem__, H)))
