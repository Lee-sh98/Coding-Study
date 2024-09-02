import sys
input = sys.stdin.readline

def distance(ax, ay, bx, by):
    return ((ax-bx)**2 + (ay-by)**2)**0.5

def solution():
    sx, sy, tx, ty = map(int, input().split())
    n = int(input())
    stars = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    for cx, cy, r in stars:
        if (r>distance(sx, sy, cx, cy))^(r>distance(tx, ty, cx, cy)):
            count += 1
    print(count)

T = int(input())
for _ in range(T):
    solution()
