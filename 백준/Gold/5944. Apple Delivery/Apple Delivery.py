import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distances = [INF]*(P+1)
    distances[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        dist, cur = heappop(q)

        if distances[cur] < dist:
            continue
        
        for node, next_dist in edges[cur]:
            cost = dist + next_dist

            if cost < distances[node]:
                distances[node] = cost
                heappush(q, (cost, node))

    return distances
    

C, P, PB, PA1, PA2 = map(int, input().split())
edges = [[] for _ in range(P+1)]

for _ in range(C):
    P1, P2, D = map(int, input().split())
    edges[P1].append((P2, D))
    edges[P2].append((P1, D))

PB_D = dijkstra(PB)
PA1_D = dijkstra(PA1)
PA2_D = dijkstra(PA2)

route1 = PB_D[PA1] + PA1_D[PA2]
route2 = PB_D[PA2] + PA2_D[PA1]

print(min(route1, route2))
    
