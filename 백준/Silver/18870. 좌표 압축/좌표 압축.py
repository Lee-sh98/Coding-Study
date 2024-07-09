import sys
input = sys.stdin.readline

N = int(input())
arr = [(idx, int(x)) for idx, x in enumerate(input().split())]
ard = {}
result = [-1]*N
for idx, x in arr:
    if x not in ard:
        ard[x] = set([idx])
    else:
        ard[x].add(idx)

for idx, k in enumerate(sorted(ard)):
    for v in ard[k]:
        result[v] = idx

    
print(*result, sep=" ")
