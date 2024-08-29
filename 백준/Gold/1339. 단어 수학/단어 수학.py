import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
total = defaultdict(int)
result = 0

for a in arr:
    for idx, v in enumerate(a[::-1]):
        total[v]+=10**idx

for i, (k, v) in enumerate(sorted(total.items(), key=lambda x: x[1], reverse=True)):
    result += v*(9-i)
print(result)
