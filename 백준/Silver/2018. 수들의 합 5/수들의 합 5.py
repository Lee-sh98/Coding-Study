import sys

N = int(sys.stdin.readline())
total = 1
result = 0

i, j = 1, 1
while i<=N:
    if total<=N:
        if total==N:
            result += 1
        j += 1
        total += j
    elif total>N:
        total -= i
        i += 1
    
print(result)
