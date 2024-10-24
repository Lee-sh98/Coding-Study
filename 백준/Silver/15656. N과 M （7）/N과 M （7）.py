import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(input().split())
arr.sort(key=int)

result = product(*[arr]*M)
for r in result:
    print(" ".join(r))
