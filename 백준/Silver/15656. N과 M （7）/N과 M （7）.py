import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())

for r in product(*[sorted(input().split(), key=int)]*M):
    print(" ".join(r))
