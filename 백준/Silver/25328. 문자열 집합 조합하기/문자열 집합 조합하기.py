import collections as x, itertools as y
*W,k=(input() for _ in range(4))
r=sorted(filter(lambda d:c[d]>=2,c:=x.Counter(y.chain(*map(lambda w:y.combinations(w,int(k)),W)))))
print(("\n".join(map("".join,r)),-1)[not r])
