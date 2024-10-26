import sys

A, B = map(int, sys.stdin.readline().split())
result = 0

factor = [0]*(B+1)
sieve = [1]*(B+1)
sieve[0] = 0
sieve[1] = 0

for i in range(2, int(B**0.5)+1):
    if sieve[i]:
        for j in range(i+i, B+1, i):
            sieve[j] = 0

prime = list(filter(sieve.__getitem__, range(B+1)))

for p in prime:
    for j in range(p, B+1, p):
        c = j
        while c and not c%p:
            factor[j] += 1
            c//=p
            
for n in range(A, B+1):
    if sieve[factor[n]]:
        result += 1

print(result)
