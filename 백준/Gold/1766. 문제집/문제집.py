import sys
from heapq import *
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
indegree = [0]*(N+1)
children = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = input()
    indegree[B] += 1
    children[A].append(B)

q = []
result = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(q, i)

while q:
    cur = heappop(q)
    result.append(cur)

    for child in children[cur]:
        indegree[child] -= 1
        if indegree[child] == 0:
            heappush(q, child)

print(*result)
