import sys
input = lambda: map(int, sys.stdin.readline().split())

n, q = input()
arr = list(input())
acc = [0]*(n+1)
for i in range(n):
    acc[i+1] = acc[i] + arr[i]

for _ in range(q):
    c, *data = input()
    if c==1:
        a, b = [d-1 for d in data]
        print(acc[b+1]-acc[a])
        arr[a], arr[b] = arr[b], arr[a]
        for i in range(a, b):
            acc[i+1] = acc[i] + arr[i]
    else:
        a, b, c, d = data
        print((acc[b]-acc[a-1])-(acc[d]-acc[c-1]))
 
