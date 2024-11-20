import sys
from collections import deque
input = sys.stdin.readline

WALL, EMPTY, JH, FIRE = "#.JF"

R, C = map(int, input().split())
maze = [[*input().rstrip()] for _ in range(R)]
q=deque()
result = "IMPOSSIBLE"
directions = [(1,0), (-1,0), (0,1), (0,-1)]
targets = [(JH, EMPTY), (FIRE, JH, EMPTY)]

for i in range(R):
    for j in range(C):
        if maze[i][j] == JH:
            q.appendleft((i,j,1))
        elif maze[i][j] == FIRE:
            q.append((i,j,1))

while q:
    x,y,time=q.popleft()
    cur=maze[x][y]
    if cur==JH and (x==0 or x==R-1 or y==0 or y==C-1):
        result = time
        break
    
    for dx,dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<R and 0<=ny<C:
            nxt=maze[nx][ny]
            for t, *u in targets:
                if cur==t and any(nxt==v for v in u):
                    maze[nx][ny]=cur
                    q.append((nx,ny,time+1))

print(result)