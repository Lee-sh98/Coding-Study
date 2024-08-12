import sys
from collections import defaultdict
from heapq import *
input = sys.stdin.readline

def dijkstra(start, end):
    distance = [float('inf')]*(N+1)
    distance[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        cur_distance, cur_node = heappop(q)
        if distance[cur_node]<cur_distance:
            continue
        for next_node, next_distance in graph[cur_node]:
            cost = cur_distance + next_distance
            if cost < distance[next_node]:
                distance[next_node] = cost
                heappush(q, (cost, next_node))
    return distance[end]

N, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())
routes = [[1, v1, v2, N], [1, v2, v1, N]]
result = []

for route in routes:
    tmp = []
    for i in range(3):
        distance = dijkstra(route[i], route[i+1])
        if distance == float('inf'):
            break
        tmp.append(distance)
    if len(tmp) == 3:
        result.append(sum(tmp))

print(min(result, default=-1))
