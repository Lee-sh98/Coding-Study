import itertools as i
r=range
n,k=[int(input())for _ in r(2)]
print(len(set(map("".join,i.permutations((input()for _ in r(n)),k)))))
