from collections import deque
q = deque(range(1,int(input())+1))
r = []
while q:r.append(str(q.popleft()));q.rotate(-1)
print(" ".join(r))