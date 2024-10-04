import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bundle, unit = 1000, 1000
for _ in range(M):
    b, u = map(int, input().split())
    bundle, unit = min(bundle, b), min(unit, u)

if bundle > unit*6:
    print(unit*N)
else:
    q, r = divmod(N, 6)
    print(q*bundle + min(bundle, r*unit))
