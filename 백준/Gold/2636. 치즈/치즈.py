import sys
from collections import deque
input = sys.stdin.readline

def padding(sx, sy):
    arr[sx][sy] = 0
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M):
                continue
            if arr[nx][ny] == -1:
                arr[nx][ny] = 0
                q.append((nx, ny))

def find_outer():
    for i in range(N):
        if arr[i][0] == -1:
            padding(i, 0)
        if arr[i][M-1] == -1:
            padding(i, M-1)

    for i in range(M):
        if arr[0][i] == -1:
            padding(0, i)
        if arr[N-1][i] == -1:
            padding(N-1, i)
def find_inner():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                inner.add((i, j))

def melt():
    melts = set()
    for x, y in cheese:
        for dx, dy in directions:
            if arr[x+dx][y+dy] == 0:
                melts.add((x, y))

    for x, y in melts:
        arr[x][y] = 0
        cheese.discard((x, y))

def fill_inner():
    fills = set()
    for x, y in inner:
        for dx, dy in directions:
            if arr[x+dx][y+dy] == 0 and (x, y) not in fills:
                fills.add((x, y))
                q = deque([(x, y)])
                while q:
                    cx, cy = q.popleft()
                    for tx, ty in directions:
                        nx, ny = cx+tx, cy+ty
                        if not(0<=nx<N and 0<=ny<M):
                            continue
                        if arr[nx][ny] == -1 and (nx, ny) not in fills:
                            fills.add((nx, ny))
                            q.append((nx, ny))

    for x, y in fills:
        arr[x][y] = 0
        inner.discard((x, y))

N, M = map(int, input().split())
arr = [[[-1, 1][a==1] for a in map(int, input().split())] for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cheese = set()
inner = set()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheese.add((i, j))

find_outer()    
find_inner()

days = 0
prev = len(cheese)
while cheese:
    prev = len(cheese)
    melt()
    fill_inner()
    days += 1

print(days)
print(prev)
