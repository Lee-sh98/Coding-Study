import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
arr = [(int(x), idx) for idx, x in enumerate(input().split())]
result = [0]*N
heapify(arr)

prev = None
acc = 0
rank = 0

while arr:
    x, idx = heappop(arr)
    if prev != x:
        rank += acc
        acc = 1
    
    result[idx] = rank
    prev = x
    
print(*result, sep=" ")
