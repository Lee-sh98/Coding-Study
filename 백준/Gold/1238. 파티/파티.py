import sys
from collections import defaultdict
from heapq import *
input = sys.stdin.readline

def dijkstra(graph, start):
    distances = [float('inf')]*(N+1)
    distances[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue
        for next_node, next_dist in graph[cur]:
            if distances[next_node] > dist + next_dist:
                distances[next_node] = dist + next_dist
                heappush(q, (dist + next_dist, next_node))
    return distances

N, M, X = map(int, input().split())

go_edges = defaultdict(list)
back_edges = defaultdict(list)

for _ in range(M):
    A, B, T = map(int, input().split())
    go_edges[B].append((A, T))
    back_edges[A].append((B, T))

go_result = dijkstra(go_edges, X)
back_result = dijkstra(back_edges, X)
result = 0

for i in filter(X.__ne__, range(1, N+1)):
    result = max(result, go_result[i]+back_result[i])

print(result)
