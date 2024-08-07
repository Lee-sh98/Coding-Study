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

visited = [0]*(N+1)
q = [(root, 0)]
result = 0

while q:
    cur, distance = q.pop()
    visited[cur] = 1
    if not any(visited[adj]==0 for adj in edges[cur]):
        result += distance
    for child in edges[cur]:
        if not visited[child]:
            q.append((child, distance + 1))
    
print(("No", "Yes")[result%2])
