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
    
    return sum(map(items.__getitem__, filter(lambda d: distances[d]<=m, range(1, n+1))))

n, m, r = map(int, input().split())
items = [0]+list(map(int, input().split()))
edges = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    edges[a].append((b, l))
    edges[b].append((a, l))

print(max(map(dijkstra, range(1, n+1))))
