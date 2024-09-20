import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distances = [INF]*(N+1)
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
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))
    K = int(input())
    friends = list(map(int, input().split()))

    results = list(dijkstra(friend) for friend in friends)
    answer, MAX = 0, INF
    for i in range(1, N+1):
        s = sum(result[i] for result in results)

        if s < MAX:
            MAX = s
            answer = i
        elif s == MAX:
            answer = min(answer, i)

    print(answer)
    
