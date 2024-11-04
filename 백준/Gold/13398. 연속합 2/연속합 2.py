import sys
input = sys.stdin.readline
INF = -int(1e9)

n = int(input())
result = a = b = INF

for m in map(int, input().split()):
    a, b = [max(a, 0)+m, max(b+m, a)]
    result = max(result, a, b)

print(result)
