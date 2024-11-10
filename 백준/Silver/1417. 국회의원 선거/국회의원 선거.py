import sys
from heapq import *
input = lambda:int(sys.stdin.readline())

N = input()
d, *arr = [input() for _ in range(N)]
arr = [0]+[-a for a in arr]
heapify(arr)
count = 0
while d<=-arr[0]:
    cur = heappop(arr)
    heappush(arr, cur + 1)    
    d += 1
    count += 1
print(count)
