import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        edges[b].append((a, s))

    distances = [INF]*(n+1)
    distances[c] = 0
    q = []
    heappush(q, (0, c))
    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue

        for node, next_dist in edges[cur]:
            cost = dist + next_dist
            if cost < distances[node]:
                distances[node] = cost
                heappush(q, (cost, node))
    
    infected = list(filter(INF.__ne__, distances))
    time = max(infected)
    print(len(infected), time)
