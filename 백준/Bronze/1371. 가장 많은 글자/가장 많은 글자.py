a={}
for c in filter(str.isalpha,open(0).read()):a[c]=a.get(c,0)+1
print(*sorted(filter(lambda x:a[x]==max(a.values()),a)),sep="")