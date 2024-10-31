import sys
from collections import Counter
input = lambda: int(sys.stdin.readline())

count = Counter(input() for _ in range(input()))
most = max(count.values())
print(min(filter(lambda c: count[c]==most, count)))
