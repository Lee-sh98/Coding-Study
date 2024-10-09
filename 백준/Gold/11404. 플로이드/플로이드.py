import sys
input = sys.stdin.readline
INF = int(1e10)

n = int(input())
m = int(input())
buses = [[INF]*n for _ in range(n)]

for i in range(n):
    buses[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    buses[a-1][b-1] = min(buses[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            buses[i][j] = min(buses[i][j], buses[i][k]+buses[k][j])

for bus in buses:
    print(" ".join(map(lambda b:str(b) if b!=INF else "0", bus)))
