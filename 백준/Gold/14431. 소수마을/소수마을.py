import sys
from heapq import *
from math import sqrt
from itertools import combinations
input = sys.stdin.readline
MAX = 9000
INF = int(1e9)

def get_distance(n1, n2):
    (x1, y1), (x2, y2) = n1, n2
    return int(sqrt((x1-x2)**2+(y1-y2)**2))

sieve = [1]*MAX
sieve[0] = 0
sieve[1] = 0
for i in range(2, int(sqrt(MAX))+1):
    for j in range(i+i, MAX, i):
        sieve[j] = 0

x1, y1, x2, y2 = map(int, input().split())
N = int(input())
nodes = [(x1, y1), (x2, y2)] + [tuple(map(int, input().split())) for _ in range(N)]

distance = [INF]*(N+2)
distance[0] = 0

edges = [[] for _ in range(N+2)]
for u, v in combinations(range(N+2), 2):
    d = get_distance(nodes[u], nodes[v])
    if sieve[d]:
        edges[u].append((v, d))
        edges[v].append((u, d))

q = [(0, 0)]
while q:
    dist, cur = heappop(q)
    if cur == 1:
        break
    
    if distance[cur] < dist:
        continue
    
    for node, ndist in edges[cur]:
        if dist+ndist < distance[node]:
            distance[node] = dist+ndist
            heappush(q, (dist+ndist, node))

result = distance[1]
print((result, -1)[result==INF])
