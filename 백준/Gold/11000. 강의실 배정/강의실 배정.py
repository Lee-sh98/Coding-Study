import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: (x[0], x[1]))
using = [lectures[0][1]]

for start, end in lectures[1:]:
    if using[0] <= start:
        heappop(using)
    heappush(using, end)

print(len(using))
