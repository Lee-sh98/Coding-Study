import sys
from heapq import *
input = sys.stdin.readline

def dijkstra(graph, start, N):
    distances = [float('inf')]*(N+1)
    distances[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue
        for next_node, next_dist in graph[cur]:
            cost = dist + next_dist
            if distances[next_node] > cost:
                distances[next_node] = cost
                heappush(q, (cost, next_node))
    return distances

N, M, X = map(int, input().split())

go_edges = [[] for _ in range(N+1)]
back_edges = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    go_edges[B].append((A, T))
    back_edges[A].append((B, T))

go_result = dijkstra(go_edges, X, N)
back_result = dijkstra(back_edges, X, N)
result = 0

for i in range(1, N+1):
    result = max(result, go_result[i]+back_result[i])

print(result)
