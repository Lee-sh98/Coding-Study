import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(sx, sy):
    distance = [[INF]*W for _ in range(H)]
    distance[sx][sy] = 0

    q = [(0, sx, sy)]
    while q:
        dist, x, y = heappop(q)
        if x==0 or y==0 or x==H-1 or y==W-1:
            return dist
        if distance[x][y] < dist:
            continue
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not(0<=nx<H and 0<=ny<W):
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heappush(q, (cost, nx, ny))

    return INF

T = int(input())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    K, W, H = map(int, input().split())

    ex,ey = 0, 0
    ship = {}
    for _ in range(K):
        name, time = input().split()
        ship[name] = int(time)

    graph = []

    for i in range(H):
        tmp = []
        for j, c in enumerate(input().rstrip()):
            if c == "E":
                ex, ey = i, j
                tmp.append(0)
            else:
                tmp.append(ship[c])

        graph.append(tmp)
    result = dijkstra(ex, ey)

    print(result)
