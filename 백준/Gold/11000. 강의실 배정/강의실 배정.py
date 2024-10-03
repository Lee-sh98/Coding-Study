import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: (x[0], x[1]))
using = [lectures[0][1]]

for i in range(1, N):
    if using[0] <= lectures[i][0]:
        heappop(using)
    heappush(using, lectures[i][1])

print(len(using))
