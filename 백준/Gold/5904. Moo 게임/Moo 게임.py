import sys

def solve(size, n, mid):
    side = (size-mid)//2
    
    if mid == 3:
        print(("m", "o")[n!=1])
    elif n <= side:
        solve(side, n, mid-1)
    elif side < n <= side+mid:
        solve(side+mid, n-side, mid-1)
    else:
        solve(side, n-side-mid, mid-1)

N = int(sys.stdin.readline())
SIZE = 3
k = 1
while SIZE < N:
    SIZE = 2*SIZE + k + 3
    k += 1

solve(SIZE, N, k+2)
