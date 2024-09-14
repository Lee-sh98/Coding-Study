import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
works = [0]*(N+1)
indegree = [0]*(N+1)
following = [[] for _ in range(N+1)]
result = [0]*(N+1)

for i in range(1, N+1):
    time, count, *precede = map(int, input().split())

    works[i] = time
    indegree[i] = count
    for pre in precede:
        following[pre].append(i)

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = works[i]

while q:
    cur = q.popleft()

    for f in following[cur]:
        indegree[f] -= 1
        result[f] = max(result[f], result[cur]+works[f])
        if indegree[f] == 0:
            q.append(f)
print(max(result))
