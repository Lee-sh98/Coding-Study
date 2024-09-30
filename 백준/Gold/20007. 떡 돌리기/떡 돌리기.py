import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    distances = [INF]*N
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
    return distances

N, M, X, Y = map(int, input().split())
edges = [[] for _ in range(N)]

for i in range(M):
    A, B, C = map(int, input().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

distances = dijkstra(Y)
valid = all(2*d <= X for d in distances)

if valid:
    total = 0
    count = 1
    distances.sort()
    i = 0
    while i < N:
        if 2*(total + distances[i]) <= X:
            total += distances[i]
        else:
            count += 1
            total = distances[i]
        i += 1
    print(count)
else:
    print(-1)
