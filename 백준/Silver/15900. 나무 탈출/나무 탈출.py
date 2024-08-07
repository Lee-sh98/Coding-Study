import sys
from collections import defaultdict, deque
input = sys.stdin.readline


N = int(input())
edges = defaultdict(list)
root = 1

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

distance = [-1]*(N+1)
leafNode = [True]*(N+1)
result = 0
q = [(root, 0)]

while q:
    cur, d = q.pop()
    distance[cur] = d
    for child in edges[cur]:
        if distance[child] == -1:
            leafNode[cur] = False
            q.append((child, d + 1))

for i in range(1, N+1):
    if leafNode[i]:
        result += distance[i]
print(("No", "Yes")[result%2])
