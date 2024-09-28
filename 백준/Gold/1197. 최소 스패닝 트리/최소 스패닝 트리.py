import sys
from heapq import *
input = sys.stdin.readline

V, E = map(int, input().split())
nodes = [0]*(V+1)
edges = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    heappush(edges[A], (C, B))
    heappush(edges[B], (C, A))


cur = 1
nodes[1] = 1
q = edges[1]
count = 1
result = 0
while count < V:
    while True:
        weight, node = heappop(q)
        if not nodes[node]:
            nodes[node] = 1
            result += weight
            count += 1
            for edge in edges[node]:
                heappush(q, edge)
            break

print(result)
