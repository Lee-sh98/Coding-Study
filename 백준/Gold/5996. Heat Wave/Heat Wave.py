import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

T,C,start,end = map(int, input().split())
edges = [[] for _ in range(T+1)]

for _ in range(C):
    a,b,c=map(int,input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))
distances = [INF]*(T+1)
distances[start] = 0

q = [(0, start)]
while q:
    dist, cur = heappop(q)
    if distances[cur] < dist:
        continue
    for node, cost in edges[cur]:
        ndist = dist + cost
        if ndist < distances[node]:
            distances[node] = ndist
            heappush(q, (ndist, node))

print(distances[end])
