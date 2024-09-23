import sys
from heapq import *
input = sys.stdin.readline

n, m, k = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

start = 1
distances = [[] for _ in range(n+1)]
q = []
heappush(distances[start], 0)
heappush(q, (0, start))

while q:
    dist, cur = heappop(q)

    for node, next_dist in edges[cur]:
        cost = dist + next_dist

        if len(distances[node]) < k:
            heappush(distances[node], -cost)
            heappush(q, (cost, node))
        elif cost < -distances[node][0]:
            heappop(distances[node])
            heappush(distances[node], -cost)
            heappush(q, (cost, node))

for i in range(1, n+1):
    if len(distances[i]) == k:
        print(-distances[i][0])
    else:
        print(-1)
