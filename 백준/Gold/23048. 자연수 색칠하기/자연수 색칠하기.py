import sys

N = int(sys.stdin.readline())
count = 1
arr = [0]*(N+1)
arr[1] = 1
for i in range(2, N+1):
    if not arr[i]:
        count += 1
        arr[i] = count
        for j in range(i+i, N+1, i):
            if not arr[j]:
                arr[j] = count

print(count)
print(*arr[1:])
