q=[*range(int(input()))]
while q:
    print(q.pop(0)+1,end=" ")
    if q:p,*q=q;q+=[p]