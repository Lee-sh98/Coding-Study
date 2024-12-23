from collections import Counter
import sys

input = sys.stdin.readline

N=int(input())
result = [0]*N
for cur in zip(*[[*map(int,input().split())] for _ in range(N)]):
    count = Counter(cur)
    for i,c in enumerate(cur):
        result[i] += (0,c)[count[c]==1]

for r in result:
    print(r)
