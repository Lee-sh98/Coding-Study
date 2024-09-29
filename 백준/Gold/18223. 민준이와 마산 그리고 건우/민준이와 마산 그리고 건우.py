import sys
from heapq import *
input = sys.stdin.readline

V, E, P = map(int, input().split())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

distances = [int(1e9)]*(V+1)
distances[1] = 0
q = [(0, 1)]

while q:
    dist, cur = heappop(q)
    if distances[cur] < dist:
        continue
    for node, next_dist in edges[cur]:
        cost = dist + next_dist
        if cost < distances[node]:
            distances[node] = cost
            heappush(q, (cost, node))

chk = [0]*(V+1)
stack = [V]
flag = False
while stack:
    cur = stack.pop()
    if cur == P:
        flag = True
        break

    if cur == 1:
        continue
        
    chk[cur] = 1
    for parent, dist in edges[cur]:
        if distances[parent] + dist == distances[cur] and not chk[parent]:
            stack.append(parent)

print(("GOOD BYE", "SAVE HIM")[flag])
