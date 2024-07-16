import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = deque(enumerate(map(int, input().split())))
result = []

while arr:
    idx, num = arr.popleft()
    result.append(idx+1)
    arr.rotate(-num+1 if num>0 else -num)
    
print(*result)
