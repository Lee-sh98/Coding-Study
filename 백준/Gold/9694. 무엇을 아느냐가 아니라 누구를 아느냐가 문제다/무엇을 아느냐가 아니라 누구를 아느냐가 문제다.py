import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF]*M
    distance[start] = 0
    route = [start]*M

    q = [(0, start)]
    while q:
        dist, cur = heappop(q)
        if distance[cur] < dist:
            continue
        for node, ndist in graph[cur]:
            cost = dist + ndist
            if cost < distance[node]:
                distance[node] = cost
                route[node] = cur
                heappush(q, (cost, node))

    if distance[M-1] == INF:
        return [-1]

    cur = M-1
    path = []
    while cur != start:
        path.append(cur)
        cur = route[cur]
    path.append(start)

    return path[::-1]
    

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]

    for _ in range(N):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))

    result = dijkstra(0)
    print(f"Case #{i}:", *result)
