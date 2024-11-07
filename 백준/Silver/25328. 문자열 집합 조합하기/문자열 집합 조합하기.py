import sys
from collections import Counter
from itertools import combinations, chain
input = sys.stdin.readline

W = [input().rstrip() for _ in range(3)]
k = int(input())
count = Counter(chain(*map(lambda w: combinations(w, k), W)))

if (result:=sorted(filter(lambda c: count[c]>=2, count))):
    print("\n".join(map("".join, result)))
else:
    print(-1)
