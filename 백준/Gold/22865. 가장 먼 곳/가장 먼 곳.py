import sys
from heapq import *
input = sys.stdin.readline
INF = float('INF')

def dijkstra(start):
    distances = [INF]*(N+1)
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

N = int(input())
A, B, C = map(int, input().split())
M = int(input())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    D, E, L = map(int, input().split())
    edges[D].append((E, L))
    edges[E].append((D, L))

AD = dijkstra(A)
BD = dijkstra(B)
CD = dijkstra(C)

result = max(range(1, N+1), key=lambda x: min(AD[x], BD[x], CD[x]))
print(result)
