import sys

S = sys.stdin.readline().rstrip()
L = len(S)
acc = [0]*(L+1)

for i in range(L):
    acc[i+1] = acc[i] + int(S[i])

result = 0
for size in range(L//2, 0, -1):
    for i in range(L-2*size+1):
        if (acc[i+size]-acc[i]) == (acc[i+2*size]-acc[i+size]):
            result = 2*size
            break

    if result:
        break

print(result)
