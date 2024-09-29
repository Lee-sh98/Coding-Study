import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e10)

def fox_run(start):
    distances = [INF]*(N+1)
    distances[start] = 0

    q = [(0, start)]
    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue

        for node, next_dist in edges[cur]:
            cost = dist + next_dist
            if cost < distances[node]:
                distances[node] = cost
                heappush(q, (cost, node))

    return distances[1:]

def wolf_run(start):
    distances = [[INF, INF] for _ in range(N+1)]
    distances[start] = [0, INF]

    q = [(0, start, 0)]
    while q:
        dist, cur, seq = heappop(q)
        if distances[cur][seq] < dist:
            continue
        
        for node, next_dist in edges[cur]:
            cost = dist+(next_dist/2, next_dist*2)[seq]
            if cost < distances[node][1-seq]:
                distances[node][1-seq] = cost
                heappush(q, (cost, node, 1-seq))
                

    return distances[1:]

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    edges[a].append((b, d))
    edges[b].append((a, d))

fox = fox_run(1)
wolf = wolf_run(1)

result = sum(map(lambda f, w: f<min(w), fox, wolf))
print(result)
