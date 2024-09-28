import sys
from heapq import *
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [0]*(V+1)
edges = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    heappush(edges[A], (C, B))
    heappush(edges[B], (C, A))

q = [(0, 1)]
count = 0
result = 0
while count < V:
    cost, cur = heappop(q)
    if visited[cur]:
        continue
    visited[cur] = 1
    result += cost
    count += 1

    for edge in edges[cur]:
        if visited[edge[1]]:
            continue
        heappush(q, edge)

print(result)
