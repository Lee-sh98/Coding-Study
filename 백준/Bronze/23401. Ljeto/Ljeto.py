import sys
input = sys.stdin.readline

n = int(input())
acquire = [-10]*8
point = [0]*2

for _ in range(n):
    t, a, b = map(int, input().split())
    point[(a-1)//4] += 100 + 50*(t-acquire[a-1]<=10)
    acquire[a-1] = t

print(*point)
