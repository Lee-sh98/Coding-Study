a={}
for c in open(0).read():a[c]=a.get(c,0)+c.isalpha()
print(*sorted(x for x in a if a[x]==max(a.values())),sep="")