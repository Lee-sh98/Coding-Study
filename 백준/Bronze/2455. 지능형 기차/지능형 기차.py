import sys
input = sys.stdin.readline

passenger = 0
result = 0

for i in range(4):
    off, on = map(int, input().split())
    passenger += on-off
    result = max(result, passenger)

print(result)
