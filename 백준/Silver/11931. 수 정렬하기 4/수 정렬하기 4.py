import sys
from collections import Counter
input = lambda:int(sys.stdin.readline())

count = Counter(input() for _ in range(input()))
for n in sorted(count, reverse=True):
    print("\n".join([str(n)]*count[n]))
