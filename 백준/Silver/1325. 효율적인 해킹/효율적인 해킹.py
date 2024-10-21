import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    visited = [0]*(N+1)
    visited[s] = 1
    result = 1

    q = deque([s])
    while q:
        for child in graph[q.popleft()]:
            if not visited[child]:
                visited[child] = 1
                result += 1
                q.append(child)
    return result

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

result = list(map(bfs, range(N+1)))

MAX = max(result)
for i in range(1, N+1):
    if result[i] == MAX:
        print(i, end = " ")
