import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for i, c in enumerate(input().split()[::-1]):
    if c=="1":
        q.appendleft(i+1)
    elif c=="2":
        a = q.popleft()
        q.appendleft(i+1)
        q.appendleft(a)
    elif c=="3":
        q.append(i+1)

print(*q)
