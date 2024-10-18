import sys
from heapq import *
input = sys.stdin.readline
INF = int(2e14)

def dijkstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0

    q = [(0, start)]
    while q:
        dist, cur = heappop(q)

        if distance[cur] < dist:
            continue
        for node, ndist in edges[cur]:
            cost = dist + ndist
            
            if cost < distance[node] and H[cur] < H[node]:
                distance[node] = cost
                heappush(q, (cost, node))
            
    return distance
    

N, M, D, E = map(int, input().split())
H = [0]+list(map(int, input().split()))
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, n = map(int, input().split())
    edges[a].append((b, n))
    edges[b].append((a, n))

HOME, KU = map(dijkstra, [1, N])

MAX = -INF
for i in range(1, N+1):
    if HOME[i] != INF and KU[i] != INF:
        achieve = H[i]*E
        energy = (HOME[i]+KU[i])*D
        MAX = max(achieve-energy, MAX)
        
print(("Impossible" , MAX)[MAX != -INF])
