import sys
input = sys.stdin.readline

def collatz(n):
    yield n
    while n!=1:
        q, r = divmod(n, 2)
        if r:
            yield (n:=3*n+1)
        else:
            yield (n:=q)

while True:
    A, B = map(int, input().split())
    if A==B==0:
        break

    pA = list(collatz(A))
    pB = list(collatz(B))

    SA, SB = len(set(pA)-set(pB)), len(set(pB)-set(pA))
    C = pA[SA]
    print(f"{A} needs {SA} steps, {B} needs {SB} steps, they meet at {C}")
