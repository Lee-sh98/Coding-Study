from collections import deque
q=deque(range(int(input())))
r=[]
while q:r+=[str(q.popleft()+1)];q.rotate(-1)
print(" ".join(r))