import sys
from heapq import *

input = sys.stdin.readline

def dijkstra(graph, start, D):
    distances = [1e9]*(D+1)
    distances[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue
        for node, next_dist in graph[cur]:
            cost = dist + next_dist
            if node<=D and distances[node]>cost:
                distances[node] = cost
                heappush(q, (cost, node))
    return distances[D]

N, D = map(int, input().split())
graph = [[(i+1, 1)] for i in range(D+1)]

for _ in range(N):
    s, e, d = map(int, input().split())
    if not(0<=s<=D and 0<=e<=D):
        continue
    graph[s].append((e, d))

result = dijkstra(graph, 0, D)
print(result)
