import sys
from collections import Counter
input = sys.stdin.readline

N, C = map(int, input().split())
counter = list(Counter(map(int, input().split())).items())
counter.sort(key=lambda x: x[1], reverse=True)

result = ""

for i, j in counter:
    print((str(i)+" ")*j, end="")
