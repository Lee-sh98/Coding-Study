import sys

input = sys.stdin.readline

N = int(input())

maxx, maxy = minx, miny = list(map(int, input().split()))

for _ in range(N-1):
    x, y = list(map(int, input().split()))
    maxx, maxy = max(x, maxx), max(y, maxy)
    minx, miny = min(x, minx), min(y, miny)

sys.stdout.write(str((maxx-minx)*(maxy-miny)))
