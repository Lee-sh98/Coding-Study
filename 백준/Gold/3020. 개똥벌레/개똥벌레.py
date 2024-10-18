import sys
input = sys.stdin.readline

N, H = map(int, input().split())
arr = [0]*(H+1)
brr = [0]*(H+1)

for i in range(N):
    cur = int(input())
    if i%2==0:
        arr[cur] += 1
    else:
        brr[cur] += 1

for i in range(H-1, 0, -1):
    arr[i] += arr[i+1]
    brr[i] += brr[i+1]

MIN, SECTION = sys.maxsize, 0

for h in range(1, H+1):
    count = arr[h] + brr[H-h+1]
    if count < MIN:
        MIN = count
        SECTION = 1
    elif count == MIN:
        SECTION += 1

print(MIN, SECTION)
