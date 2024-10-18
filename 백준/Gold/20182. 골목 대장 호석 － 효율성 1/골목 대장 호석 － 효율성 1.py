import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0
    cost = [INF]*(N+1)
    cost[start] = 0

    q = [(0, 0, start)]
    while q:
        dist, max_cost, cur = heappop(q)

        if distance[cur] < dist:
            continue
        for node, next_dist in edges[cur]:
            ndist = dist + next_dist
            
            if ndist < distance[node] and ndist <= C:
                distance[node] = ndist
                cost[node] = min(cost[node], max(max_cost, next_dist))

                heappush(q, (ndist, cost[node], node))

    return cost[B] if cost[B] != INF else -1
    
N, M, A, B, C = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

result = dijkstra(A)
print(result)
