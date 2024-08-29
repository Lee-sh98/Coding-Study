import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
total = defaultdict(int)
result = 0

for a in arr:
    for i, v in enumerate(a[::-1]):
        total[v] += 10**i

for i, v in enumerate(sorted(total.values(), reverse=True)):
    result += v*(9-i)
print(result)
