import itertools as i
k,*a=[input()for _ in range(int(input())+1)]
print(len(set(map("".join,i.permutations(a,int(k))))))
