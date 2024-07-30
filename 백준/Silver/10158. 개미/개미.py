import sys
input = sys.stdin.readline

dx, dy = 1, 1

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

tx = t%(2*w)
ty = t%(2*h)

for i in range(tx):
    x += dx
    if x == 0 or x==w:
        dx *= -1

for j in range(ty):
    y += dy
    if y==0 or y==h:
        dy *= -1

print(x, y)
