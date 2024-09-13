import sys
from heapq import *
from collections import defaultdict
input = sys.stdin.readline
INF = 100_000_000

def dijkstra(start):
    distances = [INF]*(n+1)
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


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        edges[a].append((b, d))
        edges[b].append((a, d))

    targets = [int(input()) for _ in range(t)]

    s_result = dijkstra(s)
    g_result = dijkstra(g)
    h_result = dijkstra(h)

    answer = []

    for target in targets:
        gh = s_result[g] + g_result[h] + h_result[target]
        hg = s_result[h] + h_result[g] + g_result[target]

        if s_result[target] == gh or s_result[target] == hg:
            answer.append(target)

    answer.sort()
    print(" ".join(map(str, answer)))
