import itertools as i
n,k,*a=open(0).read().split()
print(len({*map("".join,i.permutations(a,int(k)))}))
