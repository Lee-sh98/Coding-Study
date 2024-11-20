import sys
from collections import deque
input = sys.stdin.readline

def is_exit(x, y):
    return x == 0 or x==h-1 or y==0 or y==w-1

def is_valid(x, y):
    return 0<=x<h and 0<=y<w

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

            if is_valid(nx, ny):
                nxt = building[nx][ny]
                if cur == SG and nxt == EMPTY:
                    building[nx][ny] = SG
                    q.append((nx, ny, time+1))
                elif cur == FIRE and (nxt == SG or nxt==EMPTY):
                    building[nx][ny] = FIRE
                    q.append((nx, ny, time+1))
    print(result)