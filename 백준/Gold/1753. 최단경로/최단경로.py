import sys
from heapq import *
input = sys.stdin.readline
print = sys.stdout.write

def dijkstra(graph, start):
    distances = {node:float('INF') for node in graph}
    distances[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        cur_dist, cur = heappop(q)
        if distances[cur] < cur_dist:
            continue
        for next_node, d in graph[cur].items():
            next_dist = cur_dist + d
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heappush(q, (next_dist, next_node))
    return distances
    

V, E = map(int, input().split())
K = int(input())
graph = {node: {} for node in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, input().split())

    if v not in graph[u]:
        graph[u][v] = w
    else:
        graph[u][v] = min(graph[u][v], w)

distances = dijkstra(graph, K)
for i in range(1, V+1):
    print(str(distances[i]).upper()+"\n")
