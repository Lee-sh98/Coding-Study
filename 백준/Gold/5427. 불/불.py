import sys
from collections import deque
input = sys.stdin.readline

def is_exit(x, y):
    return x == 0 or x==h-1 or y==0 or y==w-1

def is_building(x, y):
    return 0<=x<h and 0<=y<w

def is_valid(x, y, *target):
    return any(map(building[x][y].__eq__,target))

def visit(x, y, nx, ny):
    building[nx][ny] = building[x][y]
    q.append((nx, ny, time+1))
EMPTY, WALL, SG, FIRE = ".#@*"

T = int(input())
for _ in range(T):
    w, h = map(int,input().split())
    building = [[*input().rstrip()] for _ in range(h)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    
    for i in range(h):
        for j in range(w):
            if building[i][j] == SG:
                q.appendleft((i, j, 1))
            elif building[i][j] == FIRE:
                q.append((i, j, 1))

    result = "IMPOSSIBLE"
    while q:
        x, y, time = q.popleft()
        cur = building[x][y]
        if cur == SG and is_exit(x, y):
            result = time
            break
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if is_building(nx, ny):
                if is_valid(x,y,SG) and is_valid(nx,ny,EMPTY):
                    visit(x,y,nx,ny)
                elif is_valid(x,y,FIRE) and is_valid(nx,ny,SG,EMPTY):
                    visit(x,y,nx,ny)
    print(result)