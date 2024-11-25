q=[*range(int(input()))]
while q:print(q.pop(0)+1,end=" ");not q and exit();p,*q=q;q+=[p]