import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
portal = {}
visited = [0]*107

for _ in range(N+M):
    a, b = map(int, input().split())
    portal[a] = b

q = deque([(1, 0)])

while q:
    cur, count = q.popleft()
    if cur==100:
        print(count)
        break
    if cur>100:
        continue

    visited[cur] = 1

    for i in range(1, 7):
        nxt = cur+i

        if visited[nxt]:
            continue
        
        if nxt in portal:
            nxt = portal[nxt]
        q.append((nxt, count + 1))
        visited[nxt] = 1
        
