import sys

arr = list(sys.stdin.readline().rstrip())

if sum(map(int, arr))%3 or "0" not in arr:
    print(-1)
else:
    print("".join(sorted(arr, reverse=True)))
