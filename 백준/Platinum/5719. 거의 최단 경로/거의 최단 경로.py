import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(edges, graph, start):
    distances = [INF]*N
    distances[start] = 0
    
    q = []
    heappush(q, (0, start))
    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue
        
        for node, next_dist in graph[cur]:
            if not edges[cur][node]:
                continue
            cost = dist + next_dist
            if cost < distances[node]:
                distances[node] = cost
                heappush(q, (cost, node))

    return distances
    

def disable_edges(distances, reversed_graph, start, end):
    stack = [end]
    while stack:
        cur = stack.pop()
        if cur == start:
            continue
        
        for parent, dist in reversed_graph[cur]:
            cost = dist + distances[parent]
            if cost == distances[cur] and edges[parent][cur]:
                edges[parent][cur] = False
                stack.append(parent)

while True:
    N, M = map(int, input().split())
    if N==0 and M==0:
        break

    S, D = map(int, input().split())
    edges = [[True]*N for _ in range(N)]
    graph = [[] for _ in range(N)]
    reversed_graph = [[] for _ in range(N)]

    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((V, P))
        reversed_graph[V].append((U, P))

    distances = dijkstra(edges, graph, S)
    disable_edges(distances, reversed_graph, S, D)
    distances = dijkstra(edges, graph, S)
    
    if distances[D] != INF:
        print(distances[D])
    else:
        print(-1)
