from collections import deque

N = int(input())
q = deque(range(1,N+1))
r = []
while q:
    r.append(str(q.popleft()))
    q.rotate(-1)
print(" ".join(r))