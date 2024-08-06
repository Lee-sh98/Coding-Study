import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
i, j = 0, n-1
arr.sort()
count = 0

while i<j<n:
    tmp = arr[i] + arr[j]
    if tmp == x:
        count += 1
        i += 1
    elif tmp<x:
        i += 1
    else:
        j -= 1

print(count)
