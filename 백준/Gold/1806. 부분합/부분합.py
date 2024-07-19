import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
length = 100000
total = 0

while s<=e:
    if total<S:
        if e>=N:
            break
        total += arr[e]
        e += 1
    else:
        total -= arr[s]
        length = min(length, e-s)
        s += 1
        
if length == 100000:
    print(0)
else:
    print(length)
