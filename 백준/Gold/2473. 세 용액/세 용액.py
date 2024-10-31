import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = abs(sum(arr[:3]))
liquid = tuple(arr[:3])
found = False
for i in range(N-2):
    l, r = i+1, N-1
    while l<r:
        cur = arr[i] + arr[l] + arr[r]
        if abs(cur) < result:
            result = abs(cur)
            liquid = (arr[i], arr[l], arr[r])

        if cur < 0:
            l += 1
        elif cur > 0:
            r -= 1
        else:
            found = True
            break
    if found:
        break

print(*sorted(liquid))
