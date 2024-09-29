import sys
sys.setrecursionlimit(10**4)

def n_queen(x):
    global result
    if x == N:
        result += 1
        return
    
    for y in range(N):
        if not column[y] and not diagonal[x+y] and not r_diagonal[x-y+N-1]:
            column[y] = True
            diagonal[x+y] = True
            r_diagonal[x-y+N-1] = True

            n_queen(x+1)

            column[y] = False
            diagonal[x+y] = False
            r_diagonal[x-y+N-1] = False

N = int(sys.stdin.readline())
column = [False]*N
diagonal = [False]*(2*N+1)
r_diagonal = [False]*(2*N+1)
result = 0
n_queen(0)
print(result)
