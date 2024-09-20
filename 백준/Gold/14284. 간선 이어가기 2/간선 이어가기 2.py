import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

s, t = map(int, input().split())
distances = [INF]*(n+1)
distances[s] = 0

q = []
heappush(q, (0, s))
while q:
    dist, cur = heappop(q)
    if distances[cur] < dist:
        continue

    for node, next_dist in edges[cur]:
        cost = dist + next_dist
        if cost < distances[node]:
            distances[node] = cost
            heappush(q, (cost, node))

print(distances[t])
