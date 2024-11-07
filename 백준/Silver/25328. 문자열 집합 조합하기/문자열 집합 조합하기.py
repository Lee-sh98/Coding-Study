import sys
from collections import Counter
from itertools import combinations
input = sys.stdin.readline

W = [input().rstrip() for _ in range(3)]
k = int(input())
count = Counter()

for w in W:
    for com in combinations(w, k):
        count[com] += 1

result = list(sorted(filter(lambda c: count[c]>=2, count)))
if result:
    for r in result:
        print("".join(r))
else:
    print(-1)
