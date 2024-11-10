import itertools as i
f=input
k,*a=[f()for _ in range(int(f())+1)]
print(len(set(map("".join,i.permutations(a,int(k))))))
