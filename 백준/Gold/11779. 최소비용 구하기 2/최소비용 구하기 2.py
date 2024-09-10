import sys
from heapq import *
input = sys.stdin.readline

def dijkstra(root):
    distances = [float('inf')]*(n+1)
    distances[root] = 0
    parents = [-1]*(n+1)

    q = []
    heappush(q, (0, root))
    while q:
        dist, cur = heappop(q)
        if distances[cur] < dist:
            continue
        for node, next_dist in edges[cur]:
            cost = dist+next_dist
            if cost<distances[node]:
                distances[node] = cost
                parents[node] = cur
                heappush(q, (cost, node))
    return distances, parents


    
    

n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
s, e = map(int, input().split())
distances,parents = dijkstra(s)
print(distances[e])

route = [e]
cur = e
while cur != s:
    cur = parents[cur]
    route.append(cur)

print(len(route))
print(*route[::-1])
