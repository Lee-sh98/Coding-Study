import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
visible = list(map(int, input().split()))
visible[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

distances = [INF]*N
distances[0] = 0

q = []
heappush(q, (0, 0))
while q:
    dist, cur = heappop(q)

    if distances[cur] < dist:
        continue
    for node, next_dist in graph[cur]:
        cost = dist + next_dist
        if cost < distances[node] and not visible[node]:
            distances[node] = cost
            heappush(q, (cost, node))

if distances[-1] != INF:
    print(distances[-1])
else:
    print(-1)
