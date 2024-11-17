(L,P),a,=[[*map(int,i.split())] for i in open(0)]
print(*map((L*P).__rsub__,a))