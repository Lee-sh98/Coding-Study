import sys
from collections import deque

def up(cur):
    return cur + U

def down(cur):
    return cur - D

def valid(cur):
    return 1<=cur<=F

F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
result = "use the stairs"
actions = [up, down]

q = deque([(S, 0)])
while q:
    cur, pushed = q.popleft()
    visited[cur] = 1
    if cur == G:
        result = pushed
        break
    for action in actions:
        next_floor = action(cur)
        if valid(next_floor) and not visited[next_floor]:
            visited[next_floor] = 1
            q.append((next_floor, pushed+1))

print(result)
