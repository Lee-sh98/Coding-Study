import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distances = [INF]*(n+1)
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
                routes[node][start] = str(cur)

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
routes = [["-"]*(n+1) for _ in range(n+1) ]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

for i in range(1, n+1):
    dijkstra(i)

for i in range(1, n+1):
    print(" ".join(routes[i][1:]))
