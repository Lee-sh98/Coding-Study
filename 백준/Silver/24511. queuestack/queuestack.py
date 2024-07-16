import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = map(int, input().split())

dq = deque([b for a, b in zip(A, B) if not a])
result = [0]*M

for i, c in enumerate(C):
    dq.appendleft(c)
    result[i] = dq.pop()
print(*result)
