import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)

def n_queen(x):
    global result
    if x == N:
        result += 1
        return
    
    for y in range(N):
        if not column[y] and not diagonal[x+y] and not r_diagonal[x-y+N-1]:
            column[y] = 1
            diagonal[x+y] = 1
            r_diagonal[x-y+N-1] = 1
            n_queen(x+1)
            column[y] = 0
            diagonal[x+y] = 0
            r_diagonal[x-y+N-1] = 0

N = int(sys.stdin.readline())
column = [0]*N
diagonal = [0]*(2*N+1)
r_diagonal = [0]*(2*N+1)
result = 0
n_queen(0)
print(result)
