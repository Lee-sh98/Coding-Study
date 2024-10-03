import sys
from heapq import *
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = int(1e10)

def dijkstra(start, end):
    global result
    distances = [INF]*(N+1)
    distances[start] = 0

    q = [(0, 0, start)]
    while q:
        max_cost, total_cost, cur = heappop(q)
        if distances[cur] < total_cost:
            continue
        if cur==end:
            result = min(result, max_cost)
        for node, next_cost in edges[cur]:
            n_max = max(max_cost, next_cost)
            n_cost = total_cost+next_cost
            if n_cost<distances[node] and n_cost<=C:
                distances[node] = n_cost
                heappush(q, (n_max, n_cost, node))
    

N, M, A, B, C = map(int, input().split())
edges = [[] for _ in range(N+1)]
result = INF
for _ in range(M):
    u, v, l = map(int, input().split())
    edges[u].append((v, l))
    edges[v].append((u, l))
dijkstra(A, B)
print((result, -1)[result==INF])
