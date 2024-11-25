q=[*range(int(input()))]
while q:print(q.pop(0)+1,end=" ");q and q.append(q.pop(0))