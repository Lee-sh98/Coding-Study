import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [0]*(F+1)
result = "use the stairs"

q = deque([S])
visited[S] = 1
while q:
    cur = q.popleft()
    if cur == G:
        result = visited[cur] - 1
        break
    for next_floor in [cur+U, cur-D]:
        if 0<next_floor<=F and not visited[next_floor]:
            q.append(next_floor)
            visited[next_floor] = visited[cur] + 1

print(result)
